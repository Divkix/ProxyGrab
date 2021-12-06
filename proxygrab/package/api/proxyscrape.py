from typing import List, Tuple, Union

from .._utils import AioHttp


async def proxyscrape(ptype: str) -> Tuple[bool, Union[List[str], str]]:
    """
    Get Proxies from Proxyscrape website.
    """
    url = f"https://api.proxyscrape.com/?request=displayproxies&proxytype={ptype}"
    text, rr = await AioHttp.get_text(url)
    if rr.status == 200:
        px = text.split("\r\n")
        proxies = list(filter(None, px))
        return True, proxies
    return False, "An error occured!\nResponse not equal to 200"
