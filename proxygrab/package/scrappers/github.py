from typing import List

from ujson import loads

from .._utils import AioHttp


async def get_github_proxies(p_type: str) -> List[str]:
    lst = []
    lst += await fate0_proxy(p_type)
    lst += await shiftytr_proxy(p_type)
    lst += await speedx_proxy(p_type)
    return lst


async def fate0_proxy(p_type: str):
    url = "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list"
    res, _ = await AioHttp.get_text(url)
    tmp_lst = [loads(pxy) for pxy in res.split("\n")[:-2]]
    try:
        p_list = [
            f"{proxy['host']}:{proxy['port']}"
            for proxy in tmp_lst
            if proxy["type"] == p_type
        ]
    except KeyError:
        p_list = []
    return p_list


async def shiftytr_proxy(p_type: str) -> List[str]:
    proxy_map = {
        "http": "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        "https": "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
        "socks4": "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
        "socks5": "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
    }

    res, _ = await AioHttp.get_text(proxy_map[p_type])
    return res.split("\n")


async def speedx_proxy(p_type: str) -> List[str]:
    proxy_map = {
        "http": "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "socks4": "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
        "socks5": "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    }

    # As this one does not have 'https' proxy
    if p_type not in proxy_map.keys():
        return []

    res, _ = await AioHttp.get_text(proxy_map[p_type])
    return res.split("\n")
