import requests


def proxylist(ptype):
    """Get Proxies from proxy-list.download"""
    url = f"https://www.proxy-list.download/api/v1/get?type={ptype}"
    r = requests.get(url)
    if r.status_code == 200:
        px = r.text
        px = px.split("\r\n")
        proxies = px[1:-2]
        return True, proxies
    return False, "An error occured!\nResponse not equal  200"
