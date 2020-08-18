import proxygrab

p1 = proxygrab.get_http()
print('HTTP:', len(p1))

p2 = proxygrab.get_https()
print('HTTPS:', len(p2))

p3 = proxygrab.get_socks4()
print('SOCKS4:', len(p3))

p4 = proxygrab.get_socks5()
print('SOCKS5:', len(p4))

p5 = proxygrab.get_proxy('http')
print('HTTP(GetProxyM):', len(p5))

p6 = proxygrab.get_proxy('https')
print('HTTPS(GetProxyM):', len(p6))

p7 = proxygrab.get_proxy('socks4')
print('SOCKS4(GetProxyM):', len(p7))

p8 = proxygrab.get_proxy('socks5')
print('SOCKS5(GetProxyM):', len(p8))