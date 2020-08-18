<h1 align="center">ProxyGrab</h2>

<p align="center">
<a href="https://pypi.org/project/proxygrab/"><img alt="PyPI" src="https://img.shields.io/pypi/v/proxygrab"></a>
<a href="https://github.com/SkuzzyxD/ProxyGrab/blob/master/LICENSE"><img alt="PyPI - License" src="https://img.shields.io/pypi/l/proxygrab"></a>
<a href="https://pepy.tech/project/proxygrab"><img alt="Downloads" src="https://pepy.tech/badge/proxygrab"></a></br>
<a href="https://github.com/SkuzzyxD/ProxyGrab/actions"><img alt="CI (pip)" src="https://github.com/SkuzzyxD/ProxyGrab/workflows/CI%20%28pip%29/badge.svg"></a>
</p>

I made this software to scrap proxies for my web scrapping and other testing purposes. This program just uses <a href='https://pypi.org/project/requests/'>requests</a> to get the response from API and return the proxies.

## Installation
```shell
pip install proxygrab --upgrade
```

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

## Credits
Proxy Server data courstey of:
* [ProxyScrape](https://proxyscrape.com/)
* [Proxy-List](https://www.proxy-list.download/)
