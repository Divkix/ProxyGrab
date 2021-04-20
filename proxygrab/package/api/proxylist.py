from .._utils import AioHttp


async def proxylist(ptype: str):
    """Get Proxies from proxy-list.download"""
    url = f"https://www.proxy-list.download/api/v1/get?type={ptype}"
    text, rr = await AioHttp.get_text(url)
    if rr.status == 200:
        px = text.split("\r\n")
        proxies = px[1:-2]
        return True, proxies
    return False, "An error occured!\nResponse not equal  200"
