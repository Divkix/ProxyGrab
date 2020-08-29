"""Main script which compiles all the functions from more different scripts"""

import json
from .api import proxyscrape, proxylist
from .scrapper import grab_proxies

""" Constants Start """
exceptions_string = (
    "Error, some causes may be:\n"
    "1. Maybe check you internet connection?\n"
    "2. No Proxies found!\n"
    "3. Maybe your IP is Temporarily Banned!"
)

method_types = ("all", "scrapper", "api")
proxy_types = ("http", "https", "socks4", "socks5")
""" Constants End """


def clean(mylist):
    """Clean Duplicate proxies from list by first converting list to dictionary and then
    extracting keys from it, as keys have unique value, there won't be any duplicates"""
    return list(dict.fromkeys(mylist))


def get_proxies_func(ptype, method):
    """Function to get proxies"""

    method = method.lower()  # Convert method name to lowercase
    ptype = ptype.lower()  # Convert proxy name to lowercase

    if method == "all":  # All Method
        status1, l1 = proxyscrape(ptype)  # Get proxies from Proxyscrape free API
        status2, l2 = proxylist(ptype)  # Get proxies from Proxylist free API
        l3 = grab_proxies(ptype)  # Get proxies from scrapper
        if not (status1 & status2):
            # If API's give error, raise Exception
            raise Exception(exceptions_string)
        all_proxies = l1 + l2 + l3

    elif method == "api":  # API Method
        status1, l1 = proxyscrape(ptype)  # Get proxies from Proxyscrape free API
        status2, l2 = proxylist(ptype)  # Get proxies from Proxylist free API
        if not (status1 & status2):
            # If API's give error, raise Exception
            raise Exception(exceptions_string)
        all_proxies = l1 + l2

    elif method == "scrapper":  # Scrapper Method
        all_proxies = grab_proxies(ptype)

    else:
        # Raise Exception if method is not in ('api', 'scrappper', 'all')
        raise Exception(f"No method {method} found!")

    # Clean proxies so that duplicates are removed from list!
    return clean(all_proxies)


# For HTTP
def get_http(method="all"):
    """Get http proxies from get_proxies_func() function"""
    return get_proxies_func("http", method)


def save_http(filename="http_proxygrab.txt", method="all"):
    """Save http proxies from get_proxies_func() function"""
    proxies = get_proxies_func("http", method)
    with open(filename, "w") as f:
        for proxy in proxies:
            f.write(f"{proxy} + '\n'")
        f.close()
    return


# For HTTPS
def get_https(method="all"):
    """Get https proxies from get_proxies_func() function"""
    return get_proxies_func("https", method)


def save_https(filename="https_proxygrab.txt", method="all"):
    """Save https proxies from get_proxies_func() function"""
    proxies = get_proxies_func("https", method)
    with open(filename, "w") as f:
        for proxy in proxies:
            f.write(f"{proxy} + '\n'")
        f.close()
    return filename


# For SOCKS4
def get_socks4(method="all"):
    """Get socks4 proxies from get_proxies_func() function"""
    return get_proxies_func("socks4", method)


def save_socks4(filename="socks4_proxygrab.txt", method="all"):
    """Save socks4 proxies from get_proxies_func() function"""
    proxies = get_proxies_func("socks4", method)
    with open(filename, "w") as f:
        for proxy in proxies:
            f.write(f"{proxy} + '\n'")
        f.close()
    return filename


# For SOCKS5
def get_socks5(method="all"):
    """Get socks5 proxies from get_proxies_func() function"""
    return get_proxies_func("socks5", method)


def save_socks5(filename="socks5_proxygrab.txt", method="all"):
    """Save socks5 proxies from get_proxies_func() function"""
    proxies = get_proxies_func("socks5", method)
    with open(filename, "w") as f:
        for proxy in proxies:
            f.write(f"{proxy} + '\n'")
        f.close()
    return filename


# For general - user defines proxy type
def get_proxy(type, method="all"):
    """Get the type of proxies we define using method from get_proxies_func() function"""
    if type not in proxy_types:
        raise Exception(f"Proxy Type {type} not found")
    return get_proxies_func(type, method)


def save_proxy(type, method="all"):
    """Save the type of proxies we define using method from get_proxies_func() function"""
    if type not in proxy_types:
        raise Exception(f"Proxy Type {type} not found")
    proxies = get_proxies_func(type, method)
    filename = f"{type}_proxygrab.txt"
    with open(filename, "w") as f:
        for proxy in proxies:
            f.write(f"{proxy} + '\n'")
        f.close()
    return filename


# For all proxy_types
# These 2 fucntions saves the proxies in dictionary in file
def get_all_proxies(method="all"):
    pdict = {}
    for i in proxy_types:
        pdict[i.upper()] = get_proxy(i, method)
    return pdict


def save_all_proxies(filename="all_proxies_proxygrab.txt", method="all"):
    pdict = {}
    for i in proxy_types:
        pdict[i.upper()] = get_proxy(i, method)
    with open(filename, "w") as f:
        f.write(str(pdict))
        f.close()
    return filename
