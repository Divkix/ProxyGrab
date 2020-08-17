import click
from proxygrab.main import get_http, get_https, get_socks4, get_socks5


@click.command()
@click.option(
    "--ptype", "-t", default="", help="Will get the specific type of proxies."
)
@click.option("--outfile", "-o", default="", help="Will save with specified filename.")
@click.option("--save", "-s", is_flag=True, help="Will save proxies to file.")
def clicmd(ptype, save, outfile):

    ptype = ptype.lower()

    if ptype == "http":
        proxies = get_http()
    elif ptype == "https":
        proxies = get_https()
    elif ptype == "socks4":
        proxies = get_socks4()
    elif ptype == "socks5":
        proxies = get_socks5()
    else:
        click.echo("Please choose a valid type from: http, https, socks4, socks5")
        return

    if not save:
        click.echo(proxies)
        click.echo("Printed Proxies to Terminal as list.")
        return
    else:
        if outfile:
            filename = outfile
        else:
            filename = f"{ptype}_proxygrab.txt"
        with open(filename, "w") as fh:
            for i in proxies:
                fh.write(str(i + "\n"))
            click.echo(f"Saved to {filename} ^_^")

    return
