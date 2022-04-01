# ProxyGrab

<p align="center">
<a href="https://proxygrab.divkix.me"><img src="https://raw.githubusercontent.com/Divkix/ProxyGrab/master/docs/img/name.png"></a>
<i>Software to scrap proxies for my web scrapping and other testing purposes.</i></br></br>
<a href="https://pypi.org/project/ProxyGrab/"><img src="https://img.shields.io/pypi/v/ProxyGrab" alt="PyPI"></a>
<a href="https://github.com/Divkix/ProxyGrab/actions"><img src="https://github.com/Divkix/ProxyGrab/workflows/CI%20%28pip%29/badge.svg" alt="CI (pip)"></a>
<a href="https://www.codacy.com/gh/Divkix/ProxyGrab/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Divkix/ProxyGrab&amp;utm_campaign=Badge_Grade"><img src="https://app.codacy.com/project/badge/Grade/b5b68ed7f04c4f639bef56df0668d289"/></a>
<a href="https://pypi.org/project/proxygrab/"><img src="https://img.shields.io/pypi/pyversions/ProxyGrab.svg" alt="Supported Python Versions"></a>
<a href="https://pepy.tech/project/ProxyGrab"><img src="https://pepy.tech/badge/ProxyGrab" alt="Downloads"></a>
</p>

I made this software to scrap proxies for my web scrapping and other testing purposes. This program just uses [aiohttp](https://pypi.org/project/aiohttp/) to get the response from API and return the proxies, also it can scrape proxies from a few sites so that it can be used without using the API.

<i><b>NOTE:</b> This library isn't designed for production use. It's advised to use your own proxies or purchase a service which provides an API. These are merely free ones that are retrieved from sites and should only be used for development or testing purposes.</br>


## Installation

The latest version of proxygrab is available via `pip`:

```shell
pip install --upgrade proxygrab
```

## Provided Proxies

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

## Documentation

https://proxygrab.divkix.me

## Contribuiting

Wanna help and improve this project?

Make sure to follow these before opening a PR:

- Make sure your PR passes the test and is formatted according to pre-commit.
- Make sure the package is working without any issues!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Thanks to

- [@JaredLGillespie](https://github.com/JaredLGillespie) for his [proxyscrape library](https://github.com/JaredLGillespie/proxyscrape) from which I took scrappers!
- Proxy Providers mentioned above
