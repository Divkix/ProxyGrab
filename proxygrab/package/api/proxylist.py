from typing import List, Tuple, Union

from .._utils import AioHttp


async def proxylist(ptype: str) -> Tuple[bool, Union[List[str], str]]:
    """
    Get Proxies from proxy-list.download
    """
    url = f"https://www.proxy-list.download/api/v1/get?type={ptype}"
    text, rr = await AioHttp.get_text(url)
    if rr.status == 200:
        px = text.split("\r\n")
        proxies = list(filter(None, px))
        return True, proxies
    return False, "An error occured!\nResponse not equal  200"
