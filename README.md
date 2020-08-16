# Proxy Grab

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Skuzzy_xD/)


I made this software to scrap proxies for my web scrapping and other testing purposes. This program just uses *requests* to get the response from API and return the proxies.

## Installation
```shell
pip install proxygrab
```

## Usage:

```py
import proxygrab

proxygrab.get_socks5()  # Returns socks5 proxylist
proxygrab.get_socks4()  # Returns socks4 proxylist
proxygrab.get_http()  # Returns http proxylist
proxygrab.get_https()  # Returns https proxylist
```

## Contribuiting

Wanna help to improve this project?

Make sure to follow these before opening a PR:
* Make sure your PR is formatted with Black
* Make sure the package is working

## Built With

* [Python](https://www.python.org/) - Programming Language

## Authors

* **Skuzzy xD** - [SkuzzyxD](https://github.com/SkuzzyxD)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## :star: Credits
Proxy Server data courstey of:
* [ProxyScrape](https://proxyscrape.com/)
* [Proxy-List](https://www.proxy-list.download/)
