import requests
from bs4 import BeautifulSoup


def grab_proxies(ptype):
    lst = []
    if ptype in ("http", "https"):
        if ptype == "https":
            lst += get_ssl_proxies()
        lst += get_anonymous_proxiesptype(ptype)
        lst += get_free_proxy_list_proxies(ptype)
        lst += get_us_proxies(ptype)
        lst += get_uk_proxies(ptype)
    else:
        lst += get_socks_proxies(ptype)
    return lst


# Only HTTPS Proxies
def get_ssl_proxies():
    url = "https://www.sslproxies.org/"
    response = requests.get(url)

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
    except:
        pass


# HTTP and HTTPS Proxies Scrapper
def get_anonymous_proxiesptype(ptype):
    url = "https://free-proxy-list.net/anonymous-proxy.html"
    response = requests.get(url)

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
    except:
        pass


def get_free_proxy_list_proxies(ptype):
    url = "http://www.free-proxy-list.net"
    response = requests.get(url)

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
    except:
        pass


def get_uk_proxies(ptype):
    url = "https://free-proxy-list.net/uk-proxy.html"
    response = requests.get(url)

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
    except:
        pass


def get_us_proxies(ptype):
    url = "https://www.us-proxy.org"
    response = requests.get(url)

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
    except:
        pass


# Socks Proxy Scrapper
def get_socks_proxies(ptype):
    url = "https://www.socks-proxy.net"
    response = requests.get(url)

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
    except:
        pass
