import click
from proxygrab.package import get_proxy


@click.command(
    context_settings=dict(help_option_names=["-h", "--help"]),
    options_metavar="<options>",
)
@click.option(
    "--type",
    "-t",
    type=str,
    help="Will get the specific type of proxies, only 4 types of proxies are availabe right now and they are: http, https, socks4, socks5",
    metavar="<proxy type>",
)
@click.option(
    "--outfile", "-o", help="Will save with specified filename.", metavar="<filename>"
)
@click.option("--save", "-s", is_flag=True, help="Will save proxies to file.")
@click.option(
    "--count",
    "-n",
    type=int,
    default=0,
    help="Number of Proxies; 0 means all",
    metavar="<int>",
    show_default=True,
)
def clicmd(type, save, outfile, count):
    """
    This a Command Line Utility from ProxyGrab which can be used to get proxies straight in your terminal or to save them to a file.
    """

    if not type:
        click.echo("No Proxy type specified, check help by proxygrab --help")
        return

    type = type.lower()
    click.echo("Fetching proxies...")

    if type in ("http", "https", "socks4", "socks5"):
        proxies = get_proxy(type)
    else:
        click.echo("Please choose a valid type from: http, https, socks4, socks5")
        return

    if count != 0:
        if count <= len(proxies):
            proxies = proxies[0:count]

    if not save:
        click.echo(proxies)
        click.echo(f"Printed {len(proxies)} proxies to Terminal as list.")
        return
    else:
        if outfile:
            filename = outfile
        else:
            filename = f"{type}_proxygrab.txt"
        with open(filename, "w") as fh:
            for i in proxies:
                fh.write(str(i + "\n"))
            click.echo(f"Saved to {filename} ^_^")
            click.echo(f"Number of proxies: {len(proxies)}")

    return
