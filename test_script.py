import proxygrab

p1 = proxygrab.get_http()
print(len(p1))

p2 = proxygrab.get_https()
print(len(p2))

p3 = proxygrab.get_socks5()
print(len(p3))

p4 = proxygrab.get_socks5()
print(len(p4))

p5 = proxygrab.get_proxy('http')
print(len(p5))

p6 = proxygrab.get_proxy('https')
print(len(p6))

p7 = proxygrab.get_proxy('socks4')
print(len(p7))

p8 = proxygrab.get_proxy('socks5')
print(len(p8))