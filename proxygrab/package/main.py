from .api import proxyscrape, proxylist
from .scrapper import grab_proxies

exceptions_string = (
    "Error, some causes may be:\n"
    "1. Maybe check you internet connection?\n"
    "2. No Proxies found!\n"
    "3. Maybe your IP is Temporarily Banned!"
)


def clean(mylist):
    """Clean Duplicate proxies from list"""
    return list(dict.fromkeys(mylist))


def get_all_proxies(ptype, method):
    """Function to get proxies"""

    if method == "all":
        status1, l1 = proxyscrape(ptype)
        status2, l2 = proxylist(ptype)
        l3 = grab_proxies(ptype)
        if (status1 & status2) == False:
            raise Exception(exceptions_string)
        all_proxies = l1 + l2 + l3

    elif method == "api":
        status1, l1 = proxyscrape(ptype)
        status2, l2 = proxylist(ptype)
        if (status1 & status2) == False:
            raise Exception(exceptions_string)
        all_proxies = l1 + l2

    elif method == "scrapper":
        all_proxies = grab_proxies(ptype)

    return clean(all_proxies)


def get_http(method="all"):
    """Wrapper to get http proxies from get_all_proxies() function"""
    if not method.lower() in ("all", "scrapper", "api"):
        raise Exception(f"No method {method} found!")
    return get_all_proxies("http", method)


def get_https(method="all"):
    """Wrapper to get https proxies from get_all_proxies() function"""
    if not method.lower() in ("all", "scrapper", "api"):
        raise Exception(f"No method {method} found!")
    return get_all_proxies("https", method)


def get_socks4(method="all"):
    """Wrapper to get socks4 proxies from get_all_proxies() function"""
    if not method.lower() in ("all", "scrapper", "api"):
        raise Exception(f"No method {method} found!")
    return get_all_proxies("socks4", method)


def get_socks5(method="all"):
    """Wrapper to get socks5 proxies from get_all_proxies() function"""
    if not method.lower() in ("all", "scrapper", "api"):
        raise Exception(f"No method {method} found!")
    return get_all_proxies("socks5", method)


def get_proxy(type, method="all"):
    """Wrapper to get the type of proxies we define using method from get_all_proxies() function"""
    if type not in ("http", "https", "socks4", "socks5"):
        raise Exception(f"Proxy Type {type} not found")
    if not method.lower() in ("all", "scrapper", "api"):
        raise Exception(f"No method {method} found!")
    return get_all_proxies(type, method)
