import proxygrab

try:
    p1 = proxygrab.get_http()
    print("HTTP:", len(p1))
except:
    pass

try:
    p2 = proxygrab.get_https()
    print("HTTPS:", len(p2))
except:
    pass

try:
    p3 = proxygrab.get_socks4()
    print("SOCKS4:", len(p3))
except:
    pass

try:
    p4 = proxygrab.get_socks5()
    print("SOCKS5:", len(p4))
except:
    pass

try:
    p5 = proxygrab.get_proxy("http")
    print("HTTP(GetProxyM):", len(p5))
except:
    pass

try:
    p6 = proxygrab.get_proxy("https")
    print("HTTPS(GetProxyM):", len(p6))
except:
    pass

try:
    p7 = proxygrab.get_proxy("socks4")
    print("SOCKS4(GetProxyM):", len(p7))
except:
    pass

try:
    p8 = proxygrab.get_proxy("socks5")
    print("SOCKS5(GetProxyM):", len(p8))
except:
    pass
