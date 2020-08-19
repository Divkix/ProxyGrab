import requests


def proxyscrape(ptype):
    """Get Proxies from Proxyscrape.com"""
    url = f"https://api.proxyscrape.com/?request=displayproxies&proxytype={ptype}"
    r = requests.get(url)
    if r.status_code == 200:
        px = r.text
        px = px.split("\r\n")
        proxies = px[1:-2]
        return True, proxies
    return False, "An error occured!\nResponse not equal to 200"
    pass
