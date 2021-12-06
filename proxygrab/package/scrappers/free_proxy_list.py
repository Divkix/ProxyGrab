from typing import List

from bs4 import BeautifulSoup

from .._utils import AioHttp


async def get_free_proxy_list_proxies(ptype: str) -> List[str]:
    url = "http://www.free-proxy-list.net"
    response, _ = await AioHttp.get_text(url)

    try:
        soup = BeautifulSoup(response.content, "lxml")
        table = soup.find("table", {"id": "proxylisttable"})
        proxies = []

        for row in table.find("tbody").find_all("tr"):
            data = list(map(lambda x: x.text, row.find_all("td")))
            host = data[0]
            port = data[1]
            version = "https" if data[6].lower() == "yes" else "http"
            if version == ptype:
                proxies.append(f"{host}:{port}")

        return proxies
    except Exception:
        return []


# HTTP and HTTPS Proxies Scrapper
async def get_anonymous_proxiesptype(ptype: str) -> List[str]:
    url = "https://free-proxy-list.net/anonymous-proxy.html"
    response, _ = await AioHttp.get_text(url)

    try:
        soup = BeautifulSoup(response.content, "lxml")
        table = soup.find("table", {"id": "proxylisttable"})
        proxies = []

        for row in table.find("tbody").find_all("tr"):
            data = list(map(lambda x: x.text, row.find_all("td")))
            host = data[0]
            port = data[1]
            version = "https" if data[6].lower() == "yes" else "http"
            if version == ptype:
                proxies.append(f"{host}:{port}")

        return proxies
    except Exception:
        return []


async def get_uk_proxies(ptype: str) -> List[str]:
    url = "https://free-proxy-list.net/uk-proxy.html"
    response, _ = await AioHttp.get_text(url)

    try:
        soup = BeautifulSoup(response.content, "lxml")
        table = soup.find("table", {"id": "proxylisttable"})
        proxies = []

        for row in table.find("tbody").find_all("tr"):
            data = list(map(lambda x: x.text, row.find_all("td")))
            host = data[0]
            port = data[1]
            version = "https" if data[6].lower() == "yes" else "http"
            if version == ptype:
                proxies.append(f"{host}:{port}")

        return proxies
    except Exception:
        return []
