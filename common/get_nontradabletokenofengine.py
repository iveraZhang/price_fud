import time
import requests

def get_nontrade():
    tokendict = {}
    tokenId1 =[]
    tokenId2 = []
    sluglist = []
    engineprice = {}
    stagprice = {}
    # url = 'https://stag-token-price.3ona.co/price/v1/all-tokens'
    url = 'https://price-api.crypto.com/price/v1/all-tokens'
    tokenlist = requests.get(url=url, params='', headers="").json()
    for i in range(len(tokenlist)):
        if tokenlist[i]["app_tradable"] is False and tokenlist[i]["exchange_tradable"] is False:
            res1 = tokenlist[i]["id"]
            res =tokenlist[i]["usd_price"]
            stagprice[res1] = res
            tokenId1.append(res1)

    time.sleep(5)
    # PriceEngineUrl = 'http://asta-crypto-token-price-engine.3ona.co/price/v1/latest'
    PriceEngineUrl = 'https://crypto-token-price-engine.crypto.com/price/v1/latest'
    headers = {"Authorization": "Basic ZnVkX3ByaWNlOiR4LVdmTTVnSGpLRERzJmQ="}
    priceEngineList = requests.get(url=PriceEngineUrl, params='', headers=headers).json()
    for token in priceEngineList["data"]:
        tokenID = token["id"]
        tokeSlug = token["slug"]
        tokenId2.append(tokenID)
        tokendict[tokenID] = tokeSlug
        engineprice[tokenID] = token["quote"]["USD"]["price"]
    commonId = list(set(tokenId1) & set(tokenId2))
    for i in commonId:
        theDifference = (float(stagprice[i]) - float(engineprice[i]))
        if theDifference == 0:
            slugg = tokendict[i]
            sluglist.append(slugg)

    return sluglist

if __name__ == '__main__':
    print(get_nontrade())


