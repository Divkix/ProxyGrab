import proxygrab

try:
    p1 = proxygrab.get_http()
    print("HTTP:", len(p1))
except Exception as ef:
    print("Error:", ef)

try:
    p2 = proxygrab.get_https()
    print("HTTPS:", len(p2))
except Exception as ef:
    print("Error:", ef)


try:
    p3 = proxygrab.get_socks4()
    print("SOCKS4:", len(p3))
except Exception as ef:
    print("Error:", ef)


try:
    p4 = proxygrab.get_socks5()
    print("SOCKS5:", len(p4))
except Exception as ef:
    print("Error:", ef)


try:
    p5 = proxygrab.get_proxy("http")
    print("HTTP(GetProxyM):", len(p5))
except Exception as ef:
    print("Error:", ef)


try:
    p6 = proxygrab.get_proxy("https")
    print("HTTPS(GetProxyM):", len(p6))
except Exception as ef:
    print("Error:", ef)


try:
    p7 = proxygrab.get_proxy("socks4")
    print("SOCKS4(GetProxyM):", len(p7))
except Exception as ef:
    print("Error:", ef)


try:
    p8 = proxygrab.get_proxy("socks5")
    print("SOCKS5(GetProxyM):", len(p8))
except Exception as ef:
    print("Error:", ef)

try:
    g = proxygrab.get_all_proxies()
    print("All(GetProxyM):", len(g))
except Exception as ef:
    print("Error:", ef)

try:
    s = proxygrab.save_all_proxies()
    print("Saved all proxies")
except Exception as ef:
    print("Error:", ef)

try:
    p1 = proxygrab.save_http()
    print("Saved http proxies")
except Exception as ef:
    print("Error:", ef)


try:
    p2 = proxygrab.save_https()
    print("Saved https proxies")
except Exception as ef:
    print("Error:", ef)


try:
    p3 = proxygrab.save_socks4()
    print("Saved socks4 proxies")
except Exception as ef:
    print("Error:", ef)


try:
    p4 = proxygrab.save_socks5()
    print("Saved socks5 proxies")
except Exception as ef:
    print("Error:", ef)


try:
    p5 = proxygrab.save_proxy("http")
    print("Saved http SaveM proxies")
except Exception as ef:
    print("Error:", ef)


try:
    p6 = proxygrab.save_proxy("https")
    print("Saved https SaveM proxies")
except Exception as ef:
    print("Error:", ef)


try:
    p7 = proxygrab.save_proxy("socks4")
    print("Saved socks4 SaveM proxies")
except Exception as ef:
    print("Error:", ef)


try:
    p8 = proxygrab.save_proxy("socks5")
    print("Saved socks5 SaveM proxies")
except Exception as ef:
    print("Error:", ef)