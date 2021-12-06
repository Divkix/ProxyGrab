"""initialise api sub-package."""

from typing import List

from .proxylist import proxylist
from .proxyscrape import proxyscrape


async def get_api_proxies(p_type: str) -> List[str]:
    lst = []
    lst += (await proxylist(p_type))[1]
    lst += (await proxyscrape(p_type))[1]
    return lst
