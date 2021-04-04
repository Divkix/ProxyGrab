"""Various Scrapper used to scrap proxies from different websites.
You can find a list of scrappers in the readme file"""

from proxygrab.package.scrappers.free_proxy_list import (
    get_anonymous_proxiesptype,
    get_free_proxy_list_proxies,
    get_uk_proxies,
)
from proxygrab.package.scrappers.socks_proxy import get_socks_proxies
from proxygrab.package.scrappers.sslproxies import get_ssl_proxies
from proxygrab.package.scrappers.us_proxy import get_us_proxies


async def grab_proxies(ptype: str):
    lst = []
    if ptype in ("http", "https"):
        if ptype == "https":
            lst += await get_ssl_proxies()
        lst += await get_anonymous_proxiesptype(ptype)
        lst += await get_free_proxy_list_proxies(ptype)
        lst += await get_us_proxies(ptype)
        lst += await get_uk_proxies(ptype)
    else:
        lst += await get_socks_proxies(ptype)
    return lst
