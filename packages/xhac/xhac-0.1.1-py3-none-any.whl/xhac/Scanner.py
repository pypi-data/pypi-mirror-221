from zeroconf import ServiceBrowser, ServiceListener, Zeroconf
import time


class SGWServer:
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port


class Listener(ServiceListener):

    def __init__(self, servers) -> None:
        super().__init__()
        self.servers = servers

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        pass

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        pass

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        self.servers.append(SGWServer(info.properties[b'name'].decode(), info.parsed_addresses()[0], info.port))


class Scanner:

    def __init__(self):
        self.servers = []

    def scan(self, duration):
        zeroconf = Zeroconf()
        listener = Listener(self.servers)
        ServiceBrowser(zeroconf, "_sgw._tcp.local.", listener)
        time.sleep(duration)
        zeroconf.close()


if __name__ == "__main__":
    scanner = Scanner()
    scanner.scan(2)
    for server in scanner.servers:
        print(f"{server.name} {server.ip} {server.port}")
