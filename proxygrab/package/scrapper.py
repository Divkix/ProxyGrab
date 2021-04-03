"""Various Scrapper used to scrap proxies from different websites.
You can find a list of scrappers in the readme file"""

from bs4 import BeautifulSoup

from proxygrab.__utils import AioHttp


async def grab_proxies(ptype):
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


# Only HTTPS Proxies
async def get_ssl_proxies():
    url = "https://www.sslproxies.org/"
    response, _ = await AioHttp.get_text(url)

    try:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", {"id": "proxylisttable"})
        proxies = []

        for row in table.find("tbody").find_all("tr"):
            data = list(map(lambda x: x.text, row.find_all("td")))
            host = data[0]
            port = data[1]
            proxies.append(f"{host}:{port}")

        return proxies
    except Exception:
        return []


# HTTP and HTTPS Proxies Scrapper
async def get_anonymous_proxiesptype(ptype):
    url = "https://free-proxy-list.net/anonymous-proxy.html"
    response, _ = await AioHttp.get_text(url)

    try:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", {"id": "proxylisttable"})
        proxies = []

        for row in table.find("tbody").find_all("tr"):
            data = list(map(lambda x: x.text, row.find_all("td")))
            host = data[0]
            port = data[1]
            if data[6].lower() == "yes":
                version = "https"
            else:
                version = "http"

            if version == ptype:
                proxies.append(f"{host}:{port}")

        return proxies
    except Exception:
        return []


async def get_free_proxy_list_proxies(ptype):
    url = "http://www.free-proxy-list.net"
    response, _ = await AioHttp.get_text(url)

    try:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", {"id": "proxylisttable"})
        proxies = []

        for row in table.find("tbody").find_all("tr"):
            data = list(map(lambda x: x.text, row.find_all("td")))
            host = data[0]
            port = data[1]
            if data[6].lower() == "yes":
                version = "https"
            else:
                version = "http"

            if version == ptype:
                proxies.append(f"{host}:{port}")

        return proxies
    except Exception:
        return []


async def get_uk_proxies(ptype):
    url = "https://free-proxy-list.net/uk-proxy.html"
    response, _ = await AioHttp.get_text(url)

    try:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", {"id": "proxylisttable"})
        proxies = []

        for row in table.find("tbody").find_all("tr"):
            data = list(map(lambda x: x.text, row.find_all("td")))
            host = data[0]
            port = data[1]
            if data[6].lower() == "yes":
                version = "https"
            else:
                version = "http"

            if version == ptype:
                proxies.append(f"{host}:{port}")

        return proxies
    except Exception:
        return []


async def get_us_proxies(ptype):
    url = "https://www.us-proxy.org"
    response, _ = await AioHttp.get_text(url)

    try:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", {"id": "proxylisttable"})
        proxies = []

        for row in table.find("tbody").find_all("tr"):
            data = list(map(lambda x: x.text, row.find_all("td")))
            host = data[0]
            port = data[1]
            if data[6].lower() == "yes":
                version = "https"
            else:
                version = "http"

            if version == ptype:
                proxies.append(f"{host}:{port}")

        return proxies
    except Exception:
        return []


# Socks Proxy Scrapper
async def get_socks_proxies(ptype):
    url = "https://www.socks-proxy.net"
    response, _ = await AioHttp.get_text(url)

    try:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", {"id": "proxylisttable"})
        proxies = []

        for row in table.find("tbody").find_all("tr"):
            data = list(map(lambda x: x.text, row.find_all("td")))
            host = data[0]
            port = data[1]
            if data[6].lower() == "socks4":
                version = "socks4"
            else:
                version = "socks5"

            if version == ptype:
                proxies.append(f"{host}:{port}")

        return proxies
    except Exception:
        return []
