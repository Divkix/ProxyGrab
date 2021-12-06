"""Main script which compiles all the functions from more different scripts."""

from typing import Dict, List

from ujson import dump

from .api import get_api_proxies
from .errors import MethodNotFound, ProxyTypeNotFound
from .scrappers import grab_proxies

# Constants Start
method_types = ("all", "scrapper", "api")
proxy_types = ("http", "https", "socks4", "socks5")
# Constants End


async def clean(mylist: list) -> List[str]:
    """
    Clean Duplicate proxies from list by first converting list to dictionary and then
    extracting keys from it, as keys have unique value, there won't be any duplicates.
    """
    return list(set(mylist))


async def get_proxies_func(ptype: str, method: str) -> List[str]:
    """
    Function to get proxies.
    """
    method = method.lower()  # Convert method name to lowercase
    ptype = ptype.lower()  # Convert proxy name to lowercase

    if method in ["all", "api"]:  # All Method
        l1 = await get_api_proxies(ptype)  # Get proxies from Proxyscrape free API
        l2 = await grab_proxies(ptype)  # Get proxies from scrapper
        all_proxies = l1 + l2

    elif method == "scrapper":  # Scrapper Method
        all_proxies = await grab_proxies(ptype)

    else:
        # Raise Exception if method is not in ('api', 'scrappper', 'all')
        raise MethodNotFound(method)

    # Clean proxies so that duplicates are removed from list!
    return await clean(all_proxies)


# For HTTP
async def get_http(method: str = "all") -> List[str]:
    """
    Get http proxies from get_proxies_func() function.
    """
    return await get_proxies_func("http", method)


async def save_http(filename: str = "http_proxygrab.txt", method: str = "all") -> str:
    """
    Save http proxies from get_proxies_func() function.
    """
    proxies = await get_proxies_func("http", method)
    with open(filename, "w+") as f:
        f.write("\n".join(proxies))
    return filename


# For HTTPS
async def get_https(method: str = "all") -> List[str]:
    """
    Get https proxies from get_proxies_func() function.
    """
    return await get_proxies_func("https", method)


async def save_https(filename: str = "https_proxygrab.txt", method: str = "all") -> str:
    """
    Save https proxies from get_proxies_func() function.
    """
    proxies = await get_proxies_func("https", method)
    with open(filename, "w+") as f:
        f.write("\n".join(proxies))
    return filename


# For SOCKS4
async def get_socks4(method: str = "all") -> List[str]:
    """
    Get socks4 proxies from get_proxies_func() function.
    """
    return await get_proxies_func("socks4", method)


async def save_socks4(
    filename: str = "socks4_proxygrab.txt",
    method: str = "all",
) -> str:
    """
    Save socks4 proxies from get_proxies_func() function.
    """
    proxies = await get_proxies_func("socks4", method)
    with open(filename, "w+") as f:
        f.write("\n".join(proxies))
    return filename


# For SOCKS5
async def get_socks5(method: str = "all") -> List[str]:
    """
    Get socks5 proxies from get_proxies_func() function.
    """
    return await get_proxies_func("socks5", method)


async def save_socks5(
    filename: str = "socks5_proxygrab.txt",
    method: str = "all",
) -> str:
    """
    Save socks5 proxies from get_proxies_func() function.
    """
    proxies = await get_proxies_func("socks5", method)
    with open(filename, "w+") as f:
        f.write("\n".join(proxies))
    return filename


# For general - user defines proxy type
async def get_proxy(ptype, method: str = "all") -> List[str]:
    """
    Get the type of proxies we define using method from get_proxies_func() function.
    """
    if ptype not in proxy_types:
        raise ProxyTypeNotFound(ptype)
    return await get_proxies_func(ptype, method)


async def save_proxy(ptype, method: str = "all") -> str:
    """
    Save the type of proxies we define using method from get_proxies_func() function.
    """
    if ptype not in proxy_types:
        raise ProxyTypeNotFound(ptype)
    proxies = await get_proxies_func(ptype, method)
    filename = f"{ptype}_proxygrab.txt"
    with open(filename, "w+") as f:
        f.write("\n".join(proxies))
    return filename


# For all proxy_types
# These 2 fucntions saves the proxies in dictionary in file
async def get_all_proxies(method: str = "all") -> Dict[str, List[str]]:
    return {i.upper(): await get_proxy(i, method) for i in proxy_types}


# save all proxies
async def save_all_proxies(
    filename: str = "all_proxies_proxygrab.txt",
    method: str = "all",
) -> str:
    pdict = {i.upper(): await get_proxy(i, method) for i in proxy_types}
    dump(pdict, filename)
    return filename
