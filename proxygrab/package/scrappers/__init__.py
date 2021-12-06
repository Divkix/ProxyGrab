"""Various Scrapper used to scrap proxies from different websites.
You can find a list of scrappers in the readme file"""

from typing import List

from .free_proxy_list import (
    get_anonymous_proxiesptype,
    get_free_proxy_list_proxies,
    get_uk_proxies,
)
from .github import get_github_proxies
from .socks_proxy import get_socks_proxies
from .sslproxies import get_ssl_proxies
from .us_proxy import get_us_proxies


async def grab_proxies(ptype: str) -> List[str]:
    lst = []
    if ptype in {"http", "https"}:
        if ptype == "https":
            lst += await get_ssl_proxies()
        lst += await get_anonymous_proxiesptype(ptype)
        lst += await get_free_proxy_list_proxies(ptype)
        lst += await get_us_proxies(ptype)
        lst += await get_uk_proxies(ptype)
    else:
        lst += await get_socks_proxies(ptype)

    # Github Scrapper
    lst += await get_github_proxies(ptype)

    return lst
