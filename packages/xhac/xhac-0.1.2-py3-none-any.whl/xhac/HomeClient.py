import sys
import socket
import srp
from .pyparser import HttpParser
from threading import Thread, Semaphore
import json
import hkdf
import hashlib
from chacha20poly1305 import ChaCha20Poly1305
import asyncio


class HTTPClient:
    def __init__(self, onEvent, onDisconnect):
        self.isSecure = False
        self.onEvent = onEvent
        self.onDisconnect = onDisconnect

        self.connected = False

        self.connectSem = Semaphore(0)
        self.disconnectSem = Semaphore(0)
        self.responseSem = None

        self.loop = asyncio.new_event_loop()
        Thread(target=self._LoopThread, daemon=True).start()

    def _LoopThread(self):
        self.loop.run_forever()

    def _CallbackThread(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def SetAccount(self, username, password):
        self.username = username
        self.password = password

    def SetHost(self, host, port):
        self.host = host
        self.port = port

    def Connect(self):
        self.loop.call_soon_threadsafe(self._Connect)
        self.connectSem.acquire()
        return self.connected

    def _Connect(self):
        if self.connected:
            self.connectSem.release()
            return

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            # Linux specific: after 10 idle seconds, start sending keepalives every 2 seconds.
            # Drop connection after 10 failed keepalives
            self.socket.setsockopt(
                socket.IPPROTO_TCP, socket.TCP_KEEPALIVE if sys.platform == 'darwin' else socket.TCP_KEEPIDLE, 10)
            self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 2)
            self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 10)

            usr = srp.User(self.username, self.password,
                           hash_alg=srp.SHA256, ng_type=srp.NG_1024)
            _, A = usr.start_authentication()

            self.socket.settimeout(5)
            self.socket.connect((self.host, self.port))

            self.Post("/srp", None)
            body = self.RecvResponse()
            body = json.loads(body)
            s, B = bytes.fromhex(body["salt"]), bytes.fromhex(body["B"])

            M = usr.process_challenge(s, B)
            self.Post("/srp", json.dumps({"A": A.hex(), "proof": M.hex()}))
            body = self.RecvResponse()
            body = json.loads(body)
            proof = bytes.fromhex(body["proof"])
            usr.verify_session(proof)

            sk = usr.get_session_key()

            kdf = hkdf.Hkdf(b"Control-Salt", sk, hash=hashlib.sha512)
            C2S_Key = kdf.expand(b"Control-Write-Encryption-Key", 32)
            self.SendCipher = ChaCha20Poly1305(C2S_Key)
            S2C_Key = kdf.expand(b"Control-Read-Encryption-Key", 32)
            self.RecvCipher = ChaCha20Poly1305(S2C_Key)

            self.sendSeq = 0
            self.recvSeq = 0

            self.isSecure = True

            self.socket.setblocking(False)

            self.recvTask = self.loop.create_task(self.RecvTask())

            self.connected = True
        except:
            self.socket.close()
        finally:
            self.connectSem.release()

    def Disconnect(self):
        self.loop.call_soon_threadsafe(self._Disconnect)
        self.disconnectSem.acquire()

    def _Disconnect(self):
        self.loop.create_task(self._DisconnectTask())

    async def _DisconnectTask(self):
        if self.connected:
            self.loop
            self.socket.close()
            self.recvTask.cancel()
            await self.recvTask
            self.connected = False
            self.isSecure = False
        self.disconnectSem.release()

    def Post(self, path, body):
        self._Send(
            (
                f"POST {path} HTTP/1.1\r\n"
                f"Content-Type: application/hap+json\r\n"
                f"Content-Length: {len(body) if body else 0}\r\n"
                f"\r\n"
                f"{body if body else ''}"
            )
        )

    def Get(self, path, params=None):
        if params:
            path += "?"
            for key, value in params.items():
                path += f"{key}={value}&"
            path = path[:-1]
        self.responseSem = Semaphore(0)
        self.loop.call_soon_threadsafe(
            self._Send, f"GET {path} HTTP/1.1\r\n\r\n")
        self.responseSem.acquire(timeout=10)
        return self.responseBody

    def Put(self, path, body):
        self.responseSem = Semaphore(0)
        self.loop.call_soon_threadsafe(
            self._Send,
            (
                f"PUT {path} HTTP/1.1\r\n"
                f"Content-Type: application/hap+json\r\n"
                f"Content-Length: {len(body)}\r\n"
                f"\r\n"
                f"{body}"
            )
        )
        self.responseSem.acquire(timeout=5)
        return self.responseBody

    def _Send(self, data):
        if self.isSecure:
            self.socket.send(len(data).to_bytes(2, "little"))

            nonce = b'\x00' * 4 + self.sendSeq.to_bytes(8, "little")
            add = len(data).to_bytes(2, "little")
            self.socket.send(self.SendCipher.encrypt(
                nonce, data.encode("utf-8"), add))

            self.sendSeq += 1
        else:
            self.socket.send(data.encode("utf-8"))

    def RecvResponse(self):
        body = b""
        p = HttpParser()
        while True:
            data = self.socket.recv(1024)
            p.execute(data, len(data))
            if p.is_partial_body():
                body += p.recv_body()
            if p.is_message_complete():
                return body.decode("utf-8")

    async def Recv(self, totalLen):
        data = b''
        recvedLen = 0
        while True:
            recvedData = await self.loop.sock_recv(self.socket, totalLen - recvedLen)
            data += recvedData
            recvedLen += len(recvedData)
            if recvedLen == totalLen:
                return data

    async def RecvTask(self):
        body = b""
        p = HttpParser()
        try:
            while True:
                len = int.from_bytes(await self.Recv(2), 'little')
                msg = await self.Recv(len + 16)

                nonce = b'\x00' * 4 + self.recvSeq.to_bytes(8, "little")
                add = len.to_bytes(2, "little")
                data = self.RecvCipher.decrypt(nonce, msg, add)

                self.recvSeq += 1

                p.execute(data, len)
                if p.is_partial_body():
                    body += p.recv_body()

                if p.is_message_complete():
                    if p.protocol == 'HTTP':
                        self.responseBody = body.decode("utf-8")
                        self.responseSem.release()
                    else:
                        self.loop.run_in_executor(None, self.onEvent, json.loads(body.decode("utf-8")))
                    body = b""
                    p = HttpParser()
        except:
            pass
        finally:
            self.socket.close()
            self.connected = False
            self.isSecure = False
            if self.responseSem:
                self.responseSem.release()
            self.loop.run_in_executor(None, self.onDisconnect)


class HomeClient(HTTPClient):
    def __init__(self, onEvent, onDisconnect):
        super().__init__(onEvent, onDisconnect)
        self.homeDB = None

    def GetHome(self):
        self.homeDB = json.loads(self.Get("/home"))
        return self.homeDB

    def SetScene(self, id):
        return self.Put("/scenes", json.dumps({"scenes": [{"sid": id}]}))

    def SetATT(self, did, iid, value):
        return self.Put("/attributes", json.dumps({"attributes": [{"did": did, "iid": iid, "value": value}]}))

    def _FindDevice(self, did):
        if self.homeDB is None:
            return None
        for device in self.homeDB["devices"]:
            if device["did"] == did:
                return device
        return None

    def _FindService(self, device, type):
        for service in device["services"]:
            if service["type"] == type:
                return service
        return None

    def _FindAttribute(self, service, type):
        for attribute in service["attributes"]:
            if attribute["type"] == type:
                return attribute
        return None

    def FindAttribute(self, did, serviceType, attributeType):
        device = self._FindDevice(did)
        if not device:
            return None
        service = self._FindService(device, serviceType)
        if not service:
            return None
        attribute = self._FindAttribute(service, attributeType)
        return attribute

    def FindAttributeType(self, did, iid):
        device = self._FindDevice(did)
        if not device:
            return None
        for service in device["services"]:
            for attribute in service["attributes"]:
                if attribute["iid"] == iid:
                    return attribute["type"]
        return None

    def SetOnOff(self, did, value):
        attribute = self.FindAttribute(did, 0x43, 0x0100)
        if not attribute:
            return None
        return self.SetATT(did, attribute["iid"], value)

    def SetBrightness(self, did, value):
        attribute = self.FindAttribute(did, 0x43, 0x0121)
        if not attribute:
            return None
        return self.SetATT(did, attribute["iid"], value)

    def SetColorTemperature(self, did, value):
        attribute = self.FindAttribute(did, 0x43, 0x01F1)
        if not attribute:
            return None
        return self.SetATT(did, attribute["iid"], value)

    def SetHSB(self, did, hue, saturation, brightness):
        attribute = self.FindAttribute(did, 0x43, 0x0123)
        if not attribute:
            return None
        return self.SetATT(did, attribute["iid"], {"hue": hue, "saturation": saturation, "brightness": brightness})
