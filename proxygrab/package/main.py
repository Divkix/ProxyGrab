"""Main script which compiles all the functions from more different scripts."""

from json import dump

from proxygrab.package.api.proxylist import proxylist
from proxygrab.package.api.proxyscrape import proxyscrape
from proxygrab.package.scrappers import grab_proxies

# Constants Start
exceptions_string = (
    "Error, some causes may be:\n"
    "1. Maybe check you internet connection?\n"
    "2. No Proxies found!\n"
    "3. Maybe your IP is Temporarily Banned!"
)

method_types = ("all", "scrapper", "api")
proxy_types = ("http", "https", "socks4", "socks5")
# Constants End


async def clean(mylist: list):
    """Clean Duplicate proxies from list by first converting list to dictionary and then
    extracting keys from it, as keys have unique value, there won't be any duplicates."""
    return list(set(mylist))


async def get_proxies_func(ptype: str, method: str):
    """Function to get proxies."""
    method = method.lower()  # Convert method name to lowercase
    ptype = ptype.lower()  # Convert proxy name to lowercase

    if method == "all":  # All Method
        status1, l1 = await proxyscrape(ptype)  # Get proxies from Proxyscrape free API
        status2, l2 = await proxylist(ptype)  # Get proxies from Proxylist free API
        l3 = await grab_proxies(ptype)  # Get proxies from scrapper
        if not (status1 & status2):
            # If API's give error, raise Exception
            raise Exception(exceptions_string)
        all_proxies = l1 + l2 + l3

    elif method == "api":  # API Method
        status1, l1 = await proxyscrape(ptype)  # Get proxies from Proxyscrape free API
        status2, l2 = await proxylist(ptype)  # Get proxies from Proxylist free API
        if not (status1 & status2):
            # If API's give error, raise Exception
            raise Exception(exceptions_string)
        all_proxies = l1 + l2

    elif method == "scrapper":  # Scrapper Method
        all_proxies = await grab_proxies(ptype)

    else:
        # Raise Exception if method is not in ('api', 'scrappper', 'all')
        raise Exception(f"No method '{method}' found!")

    # Clean proxies so that duplicates are removed from list!
    return await clean(all_proxies)


# For HTTP
async def get_http(method: str = "all"):
    """Get http proxies from get_proxies_func() function."""
    return await get_proxies_func("http", method)


async def save_http(filename: str = "http_proxygrab.txt", method: str = "all"):
    """Save http proxies from get_proxies_func() function."""
    proxies = await get_proxies_func("http", method)
    with open(filename, "w+") as f:
        f.write("\n".join(proxies))
    return filename


# For HTTPS
async def get_https(method: str = "all"):
    """Get https proxies from get_proxies_func() function."""
    return await get_proxies_func("https", method)


async def save_https(filename: str = "https_proxygrab.txt", method: str = "all"):
    """Save https proxies from get_proxies_func() function."""
    proxies = await get_proxies_func("https", method)
    with open(filename, "w+") as f:
        f.write("\n".join(proxies))
    return filename


# For SOCKS4
async def get_socks4(method: str = "all"):
    """Get socks4 proxies from get_proxies_func() function."""
    return await get_proxies_func("socks4", method)


async def save_socks4(filename: str = "socks4_proxygrab.txt", method: str = "all"):
    """Save socks4 proxies from get_proxies_func() function."""
    proxies = await get_proxies_func("socks4", method)
    with open(filename, "w+") as f:
        f.write("\n".join(proxies))
    return filename


# For SOCKS5
async def get_socks5(method: str = "all"):
    """Get socks5 proxies from get_proxies_func() function."""
    return await get_proxies_func("socks5", method)


async def save_socks5(filename: str = "socks5_proxygrab.txt", method: str = "all"):
    """Save socks5 proxies from get_proxies_func() function."""
    proxies = await get_proxies_func("socks5", method)
    with open(filename, "w+") as f:
        f.write("\n".join(proxies))
    return filename


# For general - user defines proxy type
async def get_proxy(ptype, method: str = "all"):
    """Get the type of proxies we define using method from get_proxies_func() function."""
    if ptype not in proxy_types:
        raise Exception(f"Proxy Type {ptype} not found")
    return await get_proxies_func(ptype, method)


async def save_proxy(ptype, method: str = "all"):
    """Save the type of proxies we define using method from get_proxies_func() function."""
    if ptype not in proxy_types:
        raise Exception(f"Proxy Type {ptype} not found")
    proxies = await get_proxies_func(ptype, method)
    filename = f"{ptype}_proxygrab.txt"
    with open(filename, "w+") as f:
        f.write("\n".join(proxies))
    return filename


# For all proxy_types
# These 2 fucntions saves the proxies in dictionary in file
async def get_all_proxies(method: str = "all"):
    pdict = {i.upper(): await get_proxy(i, method) for i in proxy_types}
    return pdict


# save all proxies
async def save_all_proxies(
    filename: str = "all_proxies_proxygrab.txt",
    method: str = "all",
):
    pdict = {i.upper(): await get_proxy(i, method) for i in proxy_types}
    dump(pdict, filename)
    return filename
