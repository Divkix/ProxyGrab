import json
from .api import proxyscrape, proxylist
from .scrapper import grab_proxies

exceptions_string = (
    "Error, some causes may be:\n"
    "1. Maybe check you internet connection?\n"
    "2. No Proxies found!\n"
    "3. Maybe your IP is Temporarily Banned!"
)

method_types = ("all", "scrapper", "api")
proxy_types = ("http", "https", "socks4", "socks5")


def clean(mylist):
    """Clean Duplicate proxies from list"""
    return list(dict.fromkeys(mylist))


def get_proxies_func(ptype, method):
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

    return clean(all_proxies)  # Clean proxies so that duplicates are removed from list!


# For HTTP
def get_http(method="all"):
    """Wrapper to get http proxies from get_proxies_func() function"""
    if not method.lower() in method_types:
        raise Exception(f"No method {method} found!")
    return get_proxies_func("http", method)


def save_http(filename="http_proxygrab.txt", method="all"):
    """Wrapper to save http proxies from get_proxies_func() function"""
    if not method.lower() in method_types:
        raise Exception(f"No method {method} found!")
    proxies = get_proxies_func("http", method)
    with open(filename, "w") as f:
        for proxy in proxies:
            f.write(f"{proxy} + '\n'")
        f.close()
    return


# For HTTPS
def get_https(method="all"):
    """Wrapper to get https proxies from get_proxies_func() function"""
    if not method.lower() in method_types:
        raise Exception(f"No method {method} found!")
    return get_proxies_func("https", method)


def save_https(filename="https_proxygrab.txt", method="all"):
    """Wrapper to save https proxies from get_proxies_func() function"""
    if not method.lower() in method_types:
        raise Exception(f"No method {method} found!")
    proxies = get_proxies_func("https", method)
    with open(filename, "w") as f:
        for proxy in proxies:
            f.write(f"{proxy} + '\n'")
        f.close()
    return


# For SOCKS4
def get_socks4(method="all"):
    """Wrapper to get socks4 proxies from get_proxies_func() function"""
    if not method.lower() in method_types:
        raise Exception(f"No method {method} found!")
    return get_proxies_func("socks4", method)


def save_socks4(filename="socks4_proxygrab.txt", method="all"):
    """Wrapper to save socks4 proxies from get_proxies_func() function"""
    if not method.lower() in method_types:
        raise Exception(f"No method {method} found!")
    proxies = get_proxies_func("socks4", method)
    with open(filename, "w") as f:
        for proxy in proxies:
            f.write(f"{proxy} + '\n'")
        f.close()
    return


# For SOCKS5
def get_socks5(method="all"):
    """Wrapper to get socks5 proxies from get_proxies_func() function"""
    if not method.lower() in method_types:
        raise Exception(f"No method {method} found!")
    return get_proxies_func("socks5", method)


def save_socks5(filename="socks5_proxygrab.txt", method="all"):
    """Wrapper to save socks5 proxies from get_proxies_func() function"""
    if not method.lower() in method_types:
        raise Exception(f"No method {method} found!")
    proxies = get_proxies_func("socks5", method)
    with open(filename, "w") as f:
        for proxy in proxies:
            f.write(f"{proxy} + '\n'")
        f.close()
    return


# For general - define proxy type
def get_proxy(type, method="all"):
    """Wrapper to get the type of proxies we define using method from get_proxies_func() function"""
    if type not in proxy_types:
        raise Exception(f"Proxy Type {type} not found")
    if not method.lower() in method_types:
        raise Exception(f"No method {method} found!")
    return get_proxies_func(type, method)


def save_proxy(type, method="all"):
    """Wrapper to save the type of proxies we define using method from get_proxies_func() function"""
    if type not in proxy_types:
        raise Exception(f"Proxy Type {type} not found")
    if not method.lower() in method_types:
        raise Exception(f"No method {method} found!")
    proxies = get_proxies_func(type, method)
    with open(f"{type}_proxygrab.txt", "w") as f:
        for proxy in proxies:
            f.write(f"{proxy} + '\n'")
        f.close()
    return


# For all proxy_types
def get_all_proxies(method="all"):
    if not method.lower() in method_types:
        raise Exception(f"No method {method} found!")
    pdict = {}
    for i in proxy_types:
        pdict[i.upper()] = get_proxy(i, method)
    return pdict


def save_all_proxies(filename="all_proxies_proxygrab.txt", method="all"):
    if not method.lower() in method_types:
        raise Exception(f"No method {method} found!")
    pdict = {}
    for i in proxy_types:
        pdict[i.upper()] = get_proxy(i, method)
    with open(filename, "w") as f:
        f.write(str(pdict))
        f.close()
    return
