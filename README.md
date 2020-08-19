<h1 align="center">ProxyGrab</h2>

<p align="center">
<a href="https://pypi.org/project/proxygrab/"><img alt="PyPI" src="https://img.shields.io/pypi/v/proxygrab"></a>
<a href="https://github.com/SkuzzyxD/ProxyGrab/actions"><img alt="CI (pip)" src="https://github.com/SkuzzyxD/ProxyGrab/workflows/CI%20%28pip%29/badge.svg"></a>
<a href="https://github.com/SkuzzyxD/ProxyGrab/blob/master/LICENSE"><img alt="PyPI - License" src="https://img.shields.io/pypi/l/proxygrab"></a>
<a href="https://pypi.org/project/proxygrab/"><img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/proxygrab.svg"></a>
<a href="https://pypi.org/project/proxygrab/"><img alt="" src="https://img.shields.io/pypi/pyversions/proxygrab.svg"></a>
<a href="https://pepy.tech/project/proxygrab"><img alt="Downloads" src="https://pepy.tech/badge/proxygrab"></a>
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

If no proxy type is specified, the program will show this message:
> "No Proxy type specified, check help by proxygrab --help"

## Contribuiting

Wanna help to improve this project?

Make sure to follow these before opening a PR:
* Make sure your PR is formatted with Black.
* Make sure the package is working.

## Built With

* [Python](https://www.python.org/) - Programming Language

## Authors

* **Skuzzy xD** - [SkuzzyxD](https://github.com/SkuzzyxD)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details