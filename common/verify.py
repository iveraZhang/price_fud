#所有token_url
import requests
from toolstouse.log_handle import ConsoleLogger

log = ConsoleLogger()
url = 'https://stag-token-price.3ona.co/price/v1/all-tokens'
tokenlist = requests.get(url=url, params='', headers="").json()
#只获取nontradable
nontradable = {}
duplicate = {}
list1 = []
for i in range(len(tokenlist)):
    if bool(tokenlist[i]["app_tradable"])== False or bool(tokenlist[i]["exchange_tradable"]) == False:
        nonsymbol = tokenlist[i]["symbol"]
        nontradable[nonsymbol] = tokenlist[i]["name"]

    else:
        print("000000000000000000")
log.info(f"nontradable:{nontradable}")

        # "app_tradable": true,
        # "exchange_tradable": true,
        # "defi_tradable": false,
        # "restricted_areas": [],
        # "usd_price_change_24h_abs": 0.007265,
        # "update_time": 1658117640,
    # if tokenlist[i]["app_tradable"] is False and tokenlist[i]["exchange_tradable"] is False:
    #     nonsymbol = tokenlist[i]["symbol"]
    #     nontradable[nonsymbol] = tokenlist[i]["name"]
# log.info(f"nontradable:{nontradable}")