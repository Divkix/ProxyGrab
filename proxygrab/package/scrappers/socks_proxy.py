from typing import List

from bs4 import BeautifulSoup

from .._utils import AioHttp


# Socks Proxy Scrapper
async def get_socks_proxies(ptype: str) -> List[str]:
    url = "https://www.socks-proxy.net"
    response, _ = await AioHttp.get_text(url)

    try:
        soup = BeautifulSoup(response.content, "lxml")
        table = soup.find("table", {"id": "proxylisttable"})
        proxies = []

        for row in table.find("tbody").find_all("tr"):
            data = list(map(lambda x: x.text, row.find_all("td")))
            host = data[0]
            port = data[1]
            version = "socks4" if data[6].lower() == "socks4" else "socks5"
            if version == ptype:
                proxies.append(f"{host}:{port}")

        return proxies
    except Exception:
        return []
