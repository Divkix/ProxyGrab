# FAQ
All FAQs will be mentioned here.

## What if I reach API Limit?
If you reach the API limit, you can use the `scrapper` method to get the proxies.
You API status might take upto a day to restore to normal, until then you won't be able to use the API.

## How can I get all the proxies in one file?
You can append the list on your own by making a python script, or you can wait as I will add this soon...

Till the you can use this method:
```py
import proxygrab

proxy_list = []

proxy_types = ('http', 'https', 'socks4', 'socks5')

for ptype in proxy_types:
    proxy_list.append(proxygrab.get_proxy(ptype))

print(proxy_list)
print(f"Number of Proxies: {len(proxy_list)}")
```

The script will fetch all the proxies an then print them along with their amount.

## What if the Scrappers get my IP blocked?
It is most likely to happen that you'll need to verify with Google ReCaptch while surfing the web, excess usage is not recommend at all.</br>
Also, your IP address may be blacklisted and you'll not be able to use the script again until you change your IP.

## More providers?
Yes, I'll be more providers when I find them! It would be great to get many proxies at a time.

## Does the list contain duplicate proxies?
No, since v0.2.1, the list is being cleaned to prevent duplication of proxies.
