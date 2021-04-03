# ProxyScrape Premium

ProxyScrape Premium users can also use this script!

The users can use both script and command line methods!

## Script
Users can get proxies from Premium by using the script below:

```python
from proxygrab import ProxyScrapePremium

me = ProxyScrapePremium("Your Token Here")

proxies = me.get_proxies("Proxy Type")
```

The `proxies` would be a list with the premium proxies

### Getting in different format
You can even get proxies in a different format rather than list

#### Available forms
* list: Default, no need to specify this
* normal:  Plain text
* json: JSON form, provided by proxyscrape itself

### Arguments available
* timeout
* ssl
* anonymity
* country
* limit
* format - Can be normal, json or None, If left out, then proxies would be returned in form of a list.
* age
* status
* averagetimeout
* port

You can check for these arguments from <a href="https://proxyscrape.com/api-documentation" target="_blank">Official ProxyScrape Documentation</a></br>

You can define each of them by:</br>
```python
proxies = me.get_proxies("Proxy Type", argument="value")
```

<b>Example:</b></br>

If you want proxies with status 'alive', use the following code:

```python
from proxygrab import ProxyScrapePremium

me = ProxyScrapePremium("Your Token Here")

# To get with a single argument
proxies = me.get_proxies("Proxy Type", status="alive")

# Multiple args can be supplied like this
proxies = me.get_proxies("Proxy Type", country="IN", limit="IN")
```

For countries, the 2 Digit Annotations are used!</br>
<b>Countries:</b>
```
AF, AX, AL, DZ, AS, AD, AO, AI, AQ, AG, AR, AM, AW, AU, AT, AZ, BS, BH, BD, BB, BY, BE, BZ, BJ, BM, BT, BO, BA, BW, BV, BR, IO, BN, BG, BF, BI, KH, CM, CA, CV, KY, CF, TD, CL, CN, CX, CC, CO, KM, CG, CD, CK, CR, CI, HR, CU, CY, CZ, DK, DJ, DM, DO, EC, EG, SV, GQ, ER, EE, ET, FK, FO, FJ, FI, FR, GF, PF, TF, GA, GM, GE, DE, GH, GI, GR, GL, GD, GP, GU, GT, GG, GN, GW, GY, HT, HM, VA, HN, HK, HU, IS, IN, ID, IR, IQ, IE, IM, IL, IT, JM, JP, JE, JO, KZ, KE, KI, KP, KR, KW, KG, LA, LV, LB, LS, LR, LY, LI, LT, LU, MO, MK, MG, MW, MY, MV, ML, MT, MH, MQ, MR, MU, YT, MX, FM, MD, MC, MN, ME, MS, MA, MZ, MM, NA, NR, NP, NL, AN, NC, NZ, NI, NE, NG, NU, NF, MP, NO, OM, PK, PW, PS, PA, PG, PY, PE, PH, PN, PL, PT, PR, QA, RE, RO, RU, RW, BL, SH, KN, LC, MF, PM, VC, WS, SM, ST, SA, SN, RS, SC, SL, SG, SK, SI, SB, SO, ZA, GS, ES, LK, SD, SR, SJ, SZ, SE, CH, SY, TW, TJ, TZ, TH, TL, TG, TK, TO, TT, TN, TR, TM, TC, TV, UG, UA, AE, GB, US, UM, UY, UZ, VU, VE, VN, VG, VI, WF, EH, YE, ZM, ZW
```

### Example:
If you want socks4 proxies from `United States`, which have timeout `1000`, with format `json`, anonymity as `elite`, the following piece of code would be used:

```python
from proxygrab import ProxyScrapePremium

me = ProxyScrapePremium("Your Token Here")

proxies = me.get_proxies("socks4", country="US", timeout="1000", format="json", anonymity="elite")
```

## Command Line Usage

The token can we used in Command Line too by just adding `--token YourProxyScrapeToken` to your command:
```sh
proxygrab --type https --token YourProxyScrapeToken
```

You can even save them by using:
```sh
proxygrab --type https --token YourProxyScrapeToken --save
```
