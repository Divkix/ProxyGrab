# Script Usage

You can also import the package into your script by using `import proxygrab`

## Sample code

```py
import proxygrab  # Just import the module

list = proxygrab.get_http()  # Call get_http() function to get http proxis in form of a list
```
## Getting Proxies in Script

This is for getting proxies as a list or dictinary in a python script.

### Available
You can get proxies by the following functions:

* `get_http` - Get http proxies
* `get_https` - Get https proxies
* `get_socks4` - Get socks4 proxies
* `get_socks5` - Get socks5 proxies
* `get_proxy(proxytype)` - Specify proxytype from - `http`, `https`, `socks4`, `socks5`

The above functions will use `all` as default method to grab proxies, to use a custom method, scroll down!!

### Methods available
* `all` - Get proxies from both `API` as well as `Scrapper`
* `scrapper` - Get proxies from only `Scrapper`
* `api` - Get proxies from only `api`

If you **do not** specify a method, `all` would be used as default!

## Get All Proxies
All proxies can be fetched from the function `get_all_proxies()`, it will save proxies in format of a dictionary like:
```json
{
    'HTTP': [Proxy List Here],
    'HTTPS': [Proxy List Here],
    'SOCKS4': [Proxy List Here],
    'SOCKS5': [Proxy List Here],
}
```
You can get proxies from the specific keys!

## Saving Proxies

!!! danger "Note"
    All the proxies would be saved in Current Working Directory where you are executing the script from!

These functions are used to save proxies to a file!

### Fucntions to save proxies:
* `save_http()` - Save HTTP Proxies to file `http_proxygrab.txt`
* `save_https()` - Save HTTPS Proxies to file `https_proxygrab.txt`
* `save_socks4()` - Save SOCKS4 Proxies to file `socks4_proxygrab.txt`
* `save_socks5()` - Save SOCKS5 Proxies to file `socks5_proxygrab.txt`
* `save_proxy(proxytype)` - Specify proxytype from - `http`, `https`, `socks4`, `socks5`

### Methods
Same as getting the proxies!

### Save all proxies
All proxies can be fetched from the function `save_all_proxies()`, it will be saved in form of a dictionary like:
```json
{
    'HTTP': [Proxy List Here],
    'HTTPS': [Proxy List Here],
    'SOCKS4': [Proxy List Here],
    'SOCKS5': [Proxy List Here],
}
```
The filename would be - `all_proxies_proxygrab.txt`
