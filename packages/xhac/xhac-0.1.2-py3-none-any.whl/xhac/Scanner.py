from zeroconf import ServiceBrowser, ServiceListener, Zeroconf
import time


class HomeServer:
    def __init__(self, name, ip, port, id, hostname):
        self.name = name
        self.ip = ip
        self.port = port
        self.id = id
        self.hostname = hostname


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
        self.servers.append(
            HomeServer(
                info.properties[b'name'].decode(),
                info.parsed_addresses()[0],
                info.port,
                info.properties[b'id'].decode(),
                info.server
            )
        )


class Scanner:

    def __init__(self):
        self.servers = []

    def scan(self, duration):
        zeroconf = Zeroconf()
        listener = Listener(self.servers)
        ServiceBrowser(zeroconf, "_sgw._tcp.local.", listener)
        time.sleep(duration)
        zeroconf.close()
