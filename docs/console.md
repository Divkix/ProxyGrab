# Console Usage
This page documents all the available ways for consoloe usage.</br>
To use the program via console, just type `proxygrab -h` in your command window or terminal.

## Help Command

```shell
proxygrab -h
```

```output
Usage: proxygrab <options>

  This a Command Line Utility from ProxyGrab which can be used to get
  proxies straight in your terminal or to save them to a file.

Options:
  -m, --method <method>   Method to get proxies form, available: all, api,
                            scrapper  [default: all]

  -t, --type <proxy type>   Will get the specific type of proxies, only 4
                            types of proxies are availabe right now and they
                            are: http, https, socks4, socks5

  -o, --outfile <filename>  Will save with specified filename.
  -s, --save                Will save proxies to file.
  -n, --count <int>         Number of Proxies; 0 means all  [default: 0]
  -h, --help                Show this message and exit.
```

## Usage
### To get proxies of specific type

```sh
proxygrab --type <type>
```
The following types are avaialbe: `http`, `https`, `socks4`, `socks5`


To get http proxies:
```sh
proxygrab --type http
```

The program will fetch the proxies from all sources and will return them in console.

!!! warning
    If no proxy type is specified, the program will show this message:

### To save proxies to file


```sh
proxygrab --type <type> --save
```

`--save` is a flag, which tells the program to save the proxies to a file.

To save http proxies:
```sh
proxygrab --type http --save
```

A file named `http_proxygrab.txt` will appear in the current working directory.

!!! tip
    You can use `--outfile <name>` parameter to save proxies to a custom file.

### Specifiying proxy source

You can even specifiy if you want to get proxies from either free API or using Scrappers

```sh
proxygrab --type <type> --method <method name>
```

Available methods are: `api`, `scrapper`, `all`

!!! tip
    If you do not provide a method, by default it will take `all`, which means from both `api` as well as `scrapper`.

### Specifying number of proxies

You can specify the amount of proxies you want by passing `--count` option

```sh
proxygrab --type <type> -- count <amount>
```

!!! note
    If you specify a huge amount, the scrapper will ignore it and get the maximum amount of proxies possible!