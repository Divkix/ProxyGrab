from .api import proxyscrape, proxylist
from .scrapper import grab_proxies

exceptions_string = (
    "Error, some causes may be:\n"
    "1. Maybe check you internet connection?\n"
    "2. No Proxies found!\n"
    "3. Maybe your IP is Temporarily Banned!"
)


def get_all_proxies_fucn(ptype):
    status1, l1 = proxyscrape(ptype)
    status2, l2 = proxylist(ptype)
    l3 = grab_proxies(ptype)
    if (status1 & status2) == False:
        raise Exception(exceptions_string)
    all_proxies = l1 + l2 + l3
    return all_proxies


def get_api_proxies_fucn(ptype):
    status1, l1 = proxyscrape(ptype)
    status2, l2 = proxylist(ptype)
    if (status1 & status2) == False:
        raise Exception(exceptions_string)
    all_proxies = l1 + l2
    return all_proxies


def get_scrapper_proxies_fucn(ptype):
    all_proxies = grab_proxies(ptype)
    return all_proxies


def get_http(method="all"):
    if method == "all":
        return get_all_proxies_fucn("http")
    elif method == "api":
        return get_api_proxies_fucn("http")
    elif method == "scrapper":
        return get_scrapper_proxies_fucn("http")
    else:
        raise Exception(f"No method {method} found!")


def get_https(method="all"):
    if method == "all":
        return get_all_proxies_fucn("https")
    elif method == "api":
        return get_api_proxies_fucn("https")
    elif method == "scrapper":
        return get_scrapper_proxies_fucn("https")
    else:
        raise Exception(f"No method {method} found!")


def get_socks4(method="all"):
    if method == "all":
        return get_all_proxies_fucn("socks4")
    elif method == "api":
        return get_api_proxies_fucn("socks4")
    elif method == "scrapper":
        return get_scrapper_proxies_fucn("socks4")
    else:
        raise Exception(f"No method {method} found!")


def get_socks5(method="all"):
    if method == "all":
        return get_all_proxies_fucn("socks5")
    elif method == "api":
        return get_api_proxies_fucn("socks5")
    elif method == "scrapper":
        return get_scrapper_proxies_fucn("socks5")
    else:
        raise Exception(f"No method {method} found!")


def get_proxy(type, method="all"):
    if type not in ("http", "https", "socks4", "socks5"):
        raise Exception(f"Proxy Type {type} not found")
    if method == "all":
        return get_all_proxies_fucn(type)
    elif method == "api":
        return get_api_proxies_fucn(type)
    elif method == "scrapper":
        return get_scrapper_proxies_fucn(type)
    else:
        raise Exception(f"No method {method} found!")
