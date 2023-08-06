from rich.console import Console
from rich.table import Table
from rich import box
from .HomeClient import HomeClient
from .Scanner import Scanner

def main():
    scanner = Scanner()
    print("Scanning for servers ...")
    scanner.scan(2)
    if len(scanner.servers) == 0:
        print("No server found")
        exit(1)
    for index, server in enumerate(scanner.servers):
        print(f"{index}: {server.name} {server.ip} {server.port}")
    index = int(input("- Select a server: "))
    server = scanner.servers[index]

    password = input("- Input password: ")

    def OnEvent(event):
        print(f"OnEvent: {event}")

    def OnDisconnect():
        print("Disconnected")

    homeClient = HomeClient(OnEvent, OnDisconnect)
    homeClient.SetHost(server.ip, server.port)
    homeClient.SetAccount(server.name, password)

    if not homeClient.Connect():
        print("Failed to connect")
        exit(1)

    homeDB = homeClient.GetHome()

    console = Console()

    table = Table(title="Scenes", box=box.ROUNDED)
    table.add_column("ID")
    table.add_column("Name")
    for scene in homeDB["scenes"]:
        table.add_row(f"{scene['sid']}", scene["name"])
    console.print(table)

    table = Table(title="Rooms", box=box.ROUNDED)
    table.add_column("ID")
    table.add_column("Name")
    for zone in homeDB["zones"]:
        table.add_row(f"{zone['zid']}", zone["name"])
    console.print(table)

    def FindZone(zid):
        for zone in homeDB["zones"]:
            if zone["zid"] == zid:
                return zone["name"]
        return "Unknown"

    table = Table(title="Devices", box=box.ROUNDED)
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Room")
    for device in homeDB["devices"]:
        table.add_row(f"{device['did']}", device["name"], FindZone(device["zid"]))
    console.print(table)

if __name__=="__main__":
    main()