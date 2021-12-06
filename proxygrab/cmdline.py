from asyncio import run
from functools import wraps

from click import command, echo, option

from proxygrab import get_proxy

# Constant Variables
proxy_types = ("http", "https", "socks4", "socks5")
fetch_methods = ("all", "api", "scrapper")

# List to str with ', ' as seperator - for methods
list_methods = lambda: ", ".join(fetch_methods)

# List to str with ', ' as seperator - for proxy types
list_ptypes = lambda: ", ".join(proxy_types)


# For making it run in async
def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return run(f(*args, **kwargs))

    return wrapper


@command(
    context_settings=dict(help_option_names=["-h", "--help"]),
    options_metavar="<options>",
)
@option(
    "--method",
    "-m",
    default="all",
    type=str,
    help=f"Method to get proxies form, available: {list_methods()}",
    metavar="<method>",
    show_default=True,
)
@option(
    "--type",
    "-t",
    type=str,
    help=f"Will get the specific type of proxies, only 4 types are availabe right now: {list_ptypes()}",
    metavar="<proxy type>",
)
@option(
    "--outfile",
    "-o",
    type=str,
    help="Will save with specified filename.",
    metavar="<filename>",
)
@option("--save", "-s", is_flag=True, help="Will save proxies to file.")
@option("--version", "-V", is_flag=True, help="Show version of proxygrab.")
@option(
    "--count",
    "-n",
    type=int,
    default=0,
    help="Number of Proxies; 0 means all",
    metavar="<num>",
    show_default=True,
)
@coro
async def clicmd(save: bool, type: str, outfile: str, count: int, method: str):
    """
    This a Command Line Utility from ProxyGrab which can be used to get proxies straight in your terminal or to save them to a file.
    """

    # Initially Check if user has provided the proxy type and it is in the supported formats!
    if not type:
        return echo("Check help by proxygrab --help")

    if type not in proxy_types:
        return echo(f"Only following types are supported: {list_ptypes()}")

    type = type.lower()  # Convert proxytype text to lower
    echo("Fetching proxies...")

    # Return if the method provided by user is not available
    if method not in fetch_methods:
        return echo(f"Only following methods are supported: {list_methods()}")

    # Use function to get proxies!
    # Default method is 'all'
    proxies = await get_proxy(type, method)

    # If user has defined the proxies count, scrap them only
    if count != 0 and count <= len(proxies):
        proxies = proxies[0:count]

    # If --save flag is not used, print proxies to terminal
    if not save:
        echo(proxies)
        return echo(f"Printed {len(proxies)} {type} proxies to Terminal as list.")

    # If no filename defined, use the default one
    if not outfile:
        filename = f"{type}_proxygrab.txt"

    # Write to file
    with open(filename, "w+") as f:
        for proxy in proxies:
            f.write(str(proxy + "\n"))
        f.close()

    echo(f"Saved to {filename} ^_^")
    echo(f"Number of proxies: {len(proxies)}")

    return
