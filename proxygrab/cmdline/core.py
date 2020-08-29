import click
from proxygrab import get_proxy
from proxygrab import ProxyScrapePremium

# Constant Variables
proxy_types = ["http", "https", "socks4", "socks5"]
fetch_methods = ("all", "api", "scrapper")

# List to str with ', ' as seperator - for mehods
def list_methods():
    a = ""
    for i in fetch_methods:
        a += f"{i}, "
    return a[0:-2]


# List to str with ', ' as seperator - for proxy types
def list_ptypes():
    a = ""
    for i in proxy_types:
        a += f"{i}, "
    return a[0:-2]


@click.command(
    context_settings=dict(help_option_names=["-h", "--help"]),
    options_metavar="<options>",
)
@click.option(
    "--method",
    "-m",
    default="all",
    help=f"Method to get proxies form, available: {list_methods()}",
    metavar="<method>",
    show_default=True,
)
@click.option(
    "--type",
    "-t",
    type=str,
    help=f"Will get the specific type of proxies, only 4 types are availabe right now: {list_ptypes()}",
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
    metavar="<num>",
    show_default=True,
)
@click.option(
    "--token",
    "-k",
    help="ProxyScrape Premium Token, you can use --save using it too!",
    metavar="<token>",
    default=None,
    show_default=True,
)
def clicmd(save, type: str, outfile: str, count: int, method: str, token: str):
    """
    This a Command Line Utility from ProxyGrab which can be used to get proxies straight in your terminal or to save them to a file.
    """

    # Initially Check if user has provided the proxy type and it is in the supported formats!
    if not type:
        click.echo("Check help by proxygrab --help")
        return
    if type not in proxy_types:
        click.echo(f"Only following types are supported: {list_ptypes()}")
        return

    type = type.lower()  # Convert proxytype text to lower
    click.echo("Fetching proxies...")

    # If using ProxyScrape Premium Token, then use the ProxyScrapePremium Method
    if token:
        proxies = ProxyScrapePremium(token).get_proxies(type)
        if save:
            # Write to file
            with open("proxyscrape_premium_proxygrab", "w") as f:
                for proxy in proxies:
                    f.write(str(proxy + "\n"))
                f.close()
            return
        return proxies

    # Return if the method provided by user is not available
    if method not in fetch_methods:
        click.echo(f"Only following methods are supported: {list_methods()}")
        return

    # Use function to get proxies!
    # Default method is 'all'
    proxies = get_proxy(type, method)

    # If user has defined the proxies count, scrap them on;y
    if count != 0:
        if count <= len(proxies):
            proxies = proxies[0:count]

    # If --save flag is not used, print proxies to terminal
    if not save:
        click.echo(proxies)
        click.echo(f"Printed {len(proxies)} {type} proxies to Terminal as list.")
        return

    # If no filename defined, use the default one
    if not outfile:
        filename = f"{type}_proxygrab.txt"

    # Write to file
    with open(filename, "w") as f:
        for proxy in proxies:
            f.write(str(proxy + "\n"))
        f.close()

    click.echo(f"Saved to {filename} ^_^")
    click.echo(f"Number of proxies: {len(proxies)}")

    return
