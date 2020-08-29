import requests
import json


def proxyscrape(ptype):
    """Get Proxies from Proxyscrape.com"""
    url = f"https://api.proxyscrape.com/?request=displayproxies&proxytype={ptype}"
    r = requests.get(url)
    if r.status_code == 200:
        px = r.text
        px = px.split("\r\n")
        proxies = px[1:-2]
        return True, proxies
    return False, "An error occured!\nResponse not equal to 200"
    pass


class ProxyScrapePremium:
    """Method to get proxies for Premium ProxyScrape users
    Can be used as:
    px = ProxyScrapePremium("YourSerialKeyHere")
    px.get_proxies(proxytype="http", format='json')  # Get proxies in form of json, whoch would be printed to terminal
    px.get_proxies(proxytype="http") # It will return a list
    px.get_proxies(proxytype="http", format='normal')  # It will return text as it is
    """

    def __init__(self, key: str, BASE_URL: str = "https://api.proxyscrape.com/"):
        """Initialize variables"""
        self.key = key
        self.BASE_URL = BASE_URL

    def check_key(self):
        """Check the key status by contacting the ProxyScrape API, returns if key is alive, invald or expired
        If key is valid, then continue, else raise Exception with the respeonse text from API
        """

        key_url = f"{self.BASE_URL}?request=keystatus&serialkey={self.key}"
        keystatus = requests.get(key_url)
        if not "alive" in keystatus.text.lower():
            err_text = keystatus.text
            raise Exception(err_text)
        return True

    def get_proxies(self, proxytype: str, **kwargs):
        """Get proxies from proxyscrape.net using the key"""

        ProxyScrapePremium.check_key(self)  # Check Key provided by user

        full_url = f"{self.BASE_URL}?request=getproxies"

        if not proxytype:
            raise Exception("No 'proxytype' Defined")

        full_url += f"&proxytype={proxytype}"

        timeout = kwargs.get("timeout", None)
        ssl = kwargs.get("ssl", None)
        anonymity = kwargs.get("anonymity", None)
        country = kwargs.get("country", None)
        limit = kwargs.get("limit", None)
        format = kwargs.get("format", None)
        age = kwargs.get("age", None)
        status = kwargs.get("status", None)
        averagetimeout: kwargs.get("averagetimeout", None)
        port: kwargs.get("port", None)

        """Add values to URL"""
        for key, value in kwargs.items():
            if value is not None:
                # If value is not None, add it to URL with key as parameter, else leave
                full_url += f"&{key}={value}"

        response = requests.get(full_url)
        returntext = response.text

        if format is None:
            out = returntext.split("\r\n")
            out.pop()  # Remove last empty entry '' in list
        elif format == "normal":
            out = returntext  # Text with \r\n in it
        elif format == "json":
            out = returntext  # JSON Format, only available in premium

        return out


# List of country Codes!
COUNTRY_CODE_LIST = [
    "AF",
    "AX",
    "AL",
    "DZ",
    "AS",
    "AD",
    "AO",
    "AI",
    "AQ",
    "AG",
    "AR",
    "AM",
    "AW",
    "AU",
    "AT",
    "AZ",
    "BS",
    "BH",
    "BD",
    "BB",
    "BY",
    "BE",
    "BZ",
    "BJ",
    "BM",
    "BT",
    "BO",
    "BA",
    "BW",
    "BV",
    "BR",
    "IO",
    "BN",
    "BG",
    "BF",
    "BI",
    "KH",
    "CM",
    "CA",
    "CV",
    "KY",
    "CF",
    "TD",
    "CL",
    "CN",
    "CX",
    "CC",
    "CO",
    "KM",
    "CG",
    "CD",
    "CK",
    "CR",
    "CI",
    "HR",
    "CU",
    "CY",
    "CZ",
    "DK",
    "DJ",
    "DM",
    "DO",
    "EC",
    "EG",
    "SV",
    "GQ",
    "ER",
    "EE",
    "ET",
    "FK",
    "FO",
    "FJ",
    "FI",
    "FR",
    "GF",
    "PF",
    "TF",
    "GA",
    "GM",
    "GE",
    "DE",
    "GH",
    "GI",
    "GR",
    "GL",
    "GD",
    "GP",
    "GU",
    "GT",
    "GG",
    "GN",
    "GW",
    "GY",
    "HT",
    "HM",
    "VA",
    "HN",
    "HK",
    "HU",
    "IS",
    "IN",
    "ID",
    "IR",
    "IQ",
    "IE",
    "IM",
    "IL",
    "IT",
    "JM",
    "JP",
    "JE",
    "JO",
    "KZ",
    "KE",
    "KI",
    "KP",
    "KR",
    "KW",
    "KG",
    "LA",
    "LV",
    "LB",
    "LS",
    "LR",
    "LY",
    "LI",
    "LT",
    "LU",
    "MO",
    "MK",
    "MG",
    "MW",
    "MY",
    "MV",
    "ML",
    "MT",
    "MH",
    "MQ",
    "MR",
    "MU",
    "YT",
    "MX",
    "FM",
    "MD",
    "MC",
    "MN",
    "ME",
    "MS",
    "MA",
    "MZ",
    "MM",
    "NA",
    "NR",
    "NP",
    "NL",
    "AN",
    "NC",
    "NZ",
    "NI",
    "NE",
    "NG",
    "NU",
    "NF",
    "MP",
    "NO",
    "OM",
    "PK",
    "PW",
    "PS",
    "PA",
    "PG",
    "PY",
    "PE",
    "PH",
    "PN",
    "PL",
    "PT",
    "PR",
    "QA",
    "RE",
    "RO",
    "RU",
    "RW",
    "BL",
    "SH",
    "KN",
    "LC",
    "MF",
    "PM",
    "VC",
    "WS",
    "SM",
    "ST",
    "SA",
    "SN",
    "RS",
    "SC",
    "SL",
    "SG",
    "SK",
    "SI",
    "SB",
    "SO",
    "ZA",
    "GS",
    "ES",
    "LK",
    "SD",
    "SR",
    "SJ",
    "SZ",
    "SE",
    "CH",
    "SY",
    "TW",
    "TJ",
    "TZ",
    "TH",
    "TL",
    "TG",
    "TK",
    "TO",
    "TT",
    "TN",
    "TR",
    "TM",
    "TC",
    "TV",
    "UG",
    "UA",
    "AE",
    "GB",
    "US",
    "UM",
    "UY",
    "UZ",
    "VU",
    "VE",
    "VN",
    "VG",
    "VI",
    "WF",
    "EH",
    "YE",
    "ZM",
    "ZW",
]
