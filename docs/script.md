# Script Usage

You can also import the package into your script by using `import proxygrab`

```py
import proxygrab

socks5_list = proxygrab.get_socks5()  # Returns socks5 proxylist
socks4_list = proxygrab.get_socks4()  # Returns socks4 proxylist
http_list = proxygrab.get_http()  # Returns http proxylist
https_list = proxygrab.get_https()  # Returns https proxylist

proxy_list = proxygrab.get_proxy(type)  # Type - Can any one from http, https, socks4, socks5
https_custom_list = proxygrab.get_https("scrapper")  # Get proxies only from scrappers

# get_proxy() takes 2 parameters instead of 1
proxy_custom_list = proxygrab.get_proxy(type, "scrapper")  # Same for this, where type = api, scrapper or all
```

All the variables such as `socks5_list, socks4_list, ...` are list type.

## One Liner to grab proxies:

You can even grab proxies in your terminal without using ProxyGrab Command Line Utility by using:</br>
```sh
python -c "import proxygrab; proxies = proxygrab.get_proxy('http'); print(proxies); print(len(proxies))"
```
This will grab the http proxies and print them to console, along with their amount using script type.