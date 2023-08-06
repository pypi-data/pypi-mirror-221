from rich.console import Console
from rich.table import Table
from rich import box
from typing import Union, Any
import click
from .HomeClient import HomeClient
from .Scanner import Scanner

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


def get_version():
    from pkg_resources import get_distribution
    return get_distribution("xhac").version


def print_version(context: click.Context, param: Union[click.Option, click.Parameter], value: bool) -> Any:
    """Print the version of mbed-tools."""
    if not value or context.resilient_parsing:
        return
    click.echo(get_version())
    context.exit()


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option(
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Display versions.",
)
def cli() -> None:
    """The MXOS Home Access Client Tool."""
    pass


@click.command()
@click.argument("duration", type=click.INT, default=2)
def scan(duration: int) -> None:
    """Scan for MXCHIP Home Access Server on local network.

    Arguments:

        DURATION : Scan duration time in seconds.

    Example:

        $ xhac scan 2
    """
    scanner = Scanner()
    click.echo("Scanning for servers ...")
    scanner.scan(duration)

    if len(scanner.servers) == 0:
        click.echo("No server found")
        return

    table = Table(title="Servers", box=box.ROUNDED)
    table.add_column("Name")
    table.add_column("ID")
    table.add_column("Host")
    for index, server in enumerate(scanner.servers):
        table.add_row(server.name, server.id, f"{server.ip}:{server.port}")
    console = Console()
    console.print(table)


@click.command()
@click.argument("host", type=click.STRING)
@click.argument("username", type=click.STRING)
@click.argument("password", type=click.STRING)
def load(host: str, username: str, password: str) -> None:
    """Connect to MXCHIP Home Access Server and load Home model.

    Arguments:

        HOST : Format <IP>:<Port>, 192.168.31.66:52348.

        USERNAME: Username of the server.

        PASSWORD: Password of the server.

    Example:

        $ xhac load 192.168.31.66:52348 SGW2052 mxchip123
    """

    ip, port = host.split(":")

    def OnEvent(event):
        print(f"OnEvent: {event}")

    def OnDisconnect():
        print("Disconnected")

    homeClient = HomeClient(OnEvent, OnDisconnect)
    homeClient.SetHost(ip, int(port))
    homeClient.SetAccount(username, password)

    if not homeClient.Connect():
        click.echo("Failed to connect")
        return

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
        table.add_row(f"{device['did']}", device["name"],
                      FindZone(device["zid"]))
    console.print(table)


def main():
    cli.add_command(scan, "scan")
    cli.add_command(load, "load")
    cli()


if __name__ == "__main__":
    main()
