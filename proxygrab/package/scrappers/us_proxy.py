from typing import List

from bs4 import BeautifulSoup

from .._utils import AioHttp


async def get_us_proxies(ptype: str) -> List[str]:
    url = "https://www.us-proxy.org"
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
