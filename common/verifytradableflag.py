import requests
from toolstouse.log_handle import ConsoleLogger
log = ConsoleLogger()

#symbol和name匹配
exdist = {}
appdist = {}

exurl = 'https://stag-token-price-writer.3ona.co/v1/price/fiat_rate/exchangeTradable'
extradable = requests.get(url=exurl, params='', headers="").json()

for i in extradable["data"]:
    symbol = i["symbol"]
    exdist[symbol] = i["name"]
log.info(f"exdist:{exdist}")

appurl = 'https://stag-token-price-writer.3ona.co/v1/price/fiat_rate/appTradable'
apptradable = requests.get(url=exurl, params='', headers="").json()

for i in apptradable["data"]:
    symbol = i["symbol"]
    appdist[symbol] = i["name"]
log.info(f"appdist:{appdist}")

#所有token_url
url = 'https://stag-token-price.3ona.co/price/v1/all-tokens'
tokenlist = requests.get(url=url, params='', headers="").json()
#只获取nontradable
nontradable = {}
duplicate = {}
for i in range(len(tokenlist)):
    if bool(tokenlist[i]["app_tradable"])== False and bool(tokenlist[i]["exchange_tradable"]) == False:
        nonsymbol = tokenlist[i]["symbol"]
        nontradable[nonsymbol] = tokenlist[i]["name"]
# log.info(f"nontradable:{nontradable}")
if nontradable:
    for key in nontradable.keys():
        if key in exdist:
            #如果key相等且name也相等
            if nontradable[key] == exdist[key]:
                value = exdist[key]
                duplicate[key] = value
                log.info(f"duplicate key in exdist:{key}")
                log.info(f"duplicate value/name in exdist:{value}")
        elif key in appdist:
            if nontradable[key] == appdist[key]:
                value = appdist[key]
                duplicate[key] = value
                log.info(f"duplicate key in appdist:{key}")
                log.info(f"duplicate value/name in appdist:{value}")
if not nontradable:
    print("null")

log.info(f"duplicate:{duplicate}")




