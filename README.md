<h1 align="center">ProxyGrab</h2>

<p align="center">
<a href="https://pypi.org/project/ProxyGrab/"><img alt="PyPI" src="https://img.shields.io/pypi/v/ProxyGrab"></a>
<a href="https://github.com/SkuzzyxD/ProxyGrab/actions"><img alt="CI (pip)" src="https://github.com/SkuzzyxD/ProxyGrab/workflows/CI%20%28pip%29/badge.svg"></a>
<a href="https://github.com/SkuzzyxD/ProxyGrab/blob/master/LICENSE"><img alt="PyPI - License" src="https://img.shields.io/pypi/l/ProxyGrab"></a>
<a href="https://pypi.org/project/proxygrab/"><img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/ProxyGrab.svg"></a>
<a href="https://pypi.org/project/proxygrab/"><img alt="" src="https://img.shields.io/pypi/pyversions/ProxyGrab.svg"></a>
<a href="https://pepy.tech/project/ProxyGrab"><img alt="Downloads" src="https://pepy.tech/badge/ProxyGrab"></a>
</p>

I made this software to scrap proxies for my web scrapping and other testing purposes. This program just uses <a href='https://pypi.org/project/requests/'>requests</a> to get the response from API and return the proxies.

<i>NOTE: This library isn't designed for production use. It's advised to use your own proxies or purchase a service which provides an API. These are merely free ones that are retrieved from sites and should only be used for development or testing purposes.</i>

## Installation

The latest version of proxygrab is available via `pip`:
```shell
pip install proxygrab --upgrade
```

Also, you can even download the source code and install using:
```shell
python setup.py install
```

## Provided Proxies:
<table style="width:100%">
  <tr>
    <th>Provider</th>
    <th>Proxy Types avaiable</th>
    <th>Url</th>
  </tr>
  <tr>
    <td>Proxyscrape</td>
    <td>http, https, socks4, socks5</td>
    <td>https://proxyscrape.com/</td>
  </tr>
  <tr>
    <td>Proxy-List</td>
    <td>http, https, socks4, socks5</td>
    <td>https://www.proxy-list.download/</td>
  </tr>
  <tr>
    <td>SSL Proxies</td>
    <td>https</td>
    <td>https://www.sslproxies.org/</td>
  </tr>
  <tr>
    <td>Free Proxy List</td>
    <td>http, https</td>
    <td>https://free-proxy-list.net/</td>
  </tr>
  <tr>
    <td>US Proxies</td>
    <td>http, https</td>
    <td>https://www.us-proxy.org/</td>
  </tr>
  <tr>
    <td>Socks Proxy</td>
    <td>socks4, socks5</td>
    <td>https://www.socks-proxy.net/</td>
  </tr>
</table>

## Usage:

### In Python Script

```py
import proxygrab

socks5_list = proxygrab.get_socks5()  # Returns socks5 proxylist
socks4_list = proxygrab.get_socks4()  # Returns socks4 proxylist
http_list = proxygrab.get_http()  # Returns http proxylist
https_list = proxygrab.get_https()  # Returns https proxylist
proxy_list = proxygrab.get_proxy(type)  # Type can any one from http, https, socks4, socks5

https_list = proxygrab.get_https("scrapper")  # Get proxies only from scrappers
proxy_list = proxygrab.get_proxy(type, "scrapper")  # Same for this

# Starting v2.0
# If you don't provide a method,
# 'all' would be used as default!
```

### Console

```shell
proxygrab --help
```

 * To save proxies to file:
 ```shell
proxygrab --type http --save
 ```

 * Save to custom filename:
 ```shell
proxygrab --type http --outfile custom_filename.txt --save
 ```

 * Save 100 proxies to custom filename:
 ```shell
proxygrab --type http --count 100 --outfile custom_filename.txt --save
 ```

 * Print only 5 proxies to terminal:
 ```shell
proxygrab --type http --count 5
 ```

 * Print only 5 proxies to terminal:
 ```shell
proxygrab --type http --count 5
 ```

* Take proxies only from API: (Default = all)
```shell
proxygrab --type http --method api
```

If no proxy type is specified, the program will show this message:
> "No Proxy type specified, check help by proxygrab --help"

## Contribuiting

Wanna help and improve this project?

Make sure to follow these before opening a PR:
* Make sure your PR is formatted with Black.
* Make sure the package is working.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Thanks to:
* [@JaredLGillespie](https://github.com/JaredLGillespie) for his [proxyscrape library](https://github.com/JaredLGillespie/proxyscrape) from which I took scrappers!