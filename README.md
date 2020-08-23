# ProxyGrab

<p align="center">
<a href="https://proxygrab.skuzzers.xyz"><img src="docs/img/name.png"></a>
<i>Software to scrap proxies for my web scrapping and other testing purposes.</i></br></br>
<a href="https://pypi.org/project/ProxyGrab/"><img src="https://img.shields.io/pypi/v/ProxyGrab" alt="PyPI"></a>
<a href="https://github.com/SkuzzyxD/ProxyGrab/actions"><img src="https://github.com/SkuzzyxD/ProxyGrab/workflows/CI%20%28pip%29/badge.svg" alt="CI (pip)"></a>
<a href="https://pypi.org/project/proxygrab/"><img src="https://img.shields.io/pypi/wheel/ProxyGrab.svg" alt="PyPI - Wheel"></a>
<a href="https://pypi.org/project/proxygrab/"><img src="https://img.shields.io/pypi/pyversions/ProxyGrab.svg" alt="Supported Python Versions"></a>
<a href="https://pepy.tech/project/ProxyGrab"><img src="https://pepy.tech/badge/ProxyGrab" alt="Downloads"></a>
<a href="https://proxygrab.skuzzers.xyz"><img src="https://api.netlify.com/api/v1/badges/07f64c3d-03c2-48e5-b947-0c75d38ff8ec/deploy-status" alt="Documentation"></a>
</p>

I made this software to scrap proxies for my web scrapping and other testing purposes. This program just uses [requests](https://pypi.org/project/requests/) to get the response from API and return the proxies.

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

## Documentation:
https://proxygrab.skuzzers.xyz

## Contribuiting

Wanna help and improve this project?

Make sure to follow these before opening a PR:
* Make sure your PR is formatted with Black.
* Make sure the package is working.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Thanks to:
* [@JaredLGillespie](https://github.com/JaredLGillespie) for his [proxyscrape library](https://github.com/JaredLGillespie/proxyscrape) from which I took scrappers!
* Proxy Providers mentioned above
