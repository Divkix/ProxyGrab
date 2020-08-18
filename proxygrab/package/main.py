from .sites import proxyscrape, proxylist


def get_proxies_fucn(ptype):
    status1, l1 = proxyscrape(ptype)
    status2, l2 = proxylist(ptype)
    if (status1 & status2) == False:
        raise Exception("Error!\nMaybe check you internet connection?")
    all_proxies = l1 + l2
    return all_proxies


def get_http():
    return get_proxies_fucn("http")


def get_https():
    return get_proxies_fucn("https")


def get_socks5():
    return get_proxies_fucn("socks5")


def get_socks4():
    return get_proxies_fucn("socks4")


def get_proxy(type):
    return get_proxies_fucn(type)
