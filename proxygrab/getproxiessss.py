from .proxyscrape import proxyscrape
from .proxylist import proxylist


def get_proxies(ptype):
    status1, l1 = proxyscrape(ptype)
    status2, l2 = proxylist(ptype)
    if (status1 & status2) == False:
        raise Exception("Error!\nMaybe check you internet connection?")
    all_proxies = l1 + l2
    return all_proxies


def get_http():
    proxies = get_proxies("http")
    return proxies


def get_https():
    proxies = get_proxies("https")
    return proxies


def get_socks5():
    proxies = get_proxies("socks5")
    return proxies


def get_socks4():
    proxies = get_proxies("socks4")
    return proxies
