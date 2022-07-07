import requests

def checkTheValueWithCMC():
    CMCUrl = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {"X-CMC_PRO_API_KEY": "86d41b13-5967-4435-bb39-cafa449da944"}
    CMCList = requests.get(url=CMCUrl, params='', headers=headers).json()

    PriceEngineUrl = 'http://asta-crypto-token-price-engine.3ona.co/price/v1/latest'
    headers = {"Authorization": "Basic YXN0YV9mdWRfcHJpY2U6UU4sMmtReThURzJ5VyNELQ=="}
    priceEngineList = requests.get(url=PriceEngineUrl, params='', headers=headers).json()

    CMCTokenPrice = {}
    priceEngineTokenPrice = {}
    tokenSlug = {}
    # outOfListSlug = []
    theTokenUpatateTime = {}
    moreThanTheAcceptPercentageList = []
    for i in range(len(CMCList["data"])):
        tokenID = CMCList["data"][i]["id"]
        tokeSlug = CMCList["data"][i]["slug"]
        CMCtokenPrice = CMCList["data"][i]["quote"]["USD"]["price"]
        tokenUpdateTime = CMCList["data"][i]["quote"]["USD"]["last_updated"]
        CMCTokenPrice[tokenID] = CMCtokenPrice
        theTokenUpatateTime[tokenID] = tokenUpdateTime
        tokenSlug[tokenID] = tokeSlug

    for j in range(len(priceEngineList["data"])):
        tokenID = priceEngineList["data"][j]["id"]
        tokenPrice = priceEngineList["data"][j]["quote"]["USD"]["price"]
        priceEngineTokenPrice[tokenID] = tokenPrice

    for key in CMCTokenPrice.keys():
        if key in priceEngineTokenPrice:
            theDifference = (float(CMCTokenPrice[key]) - float(priceEngineTokenPrice[key])) / float(
                priceEngineTokenPrice[key])
            if -0.04 < theDifference < 0.04:
                #写到文档里
                print(theDifference)
                continue
            else:
                # 写到文档里,id,slug,difference,update time
                print("fail")
                OutOfLimit = "{},slug:{},difference:{},tokenLastUpdateTime:{}" \
                    .format(key,tokenSlug[key],theDifference,theTokenUpatateTime[key])
                moreThanTheAcceptPercentageList.append(OutOfLimit)
    return moreThanTheAcceptPercentageList

def checkTheValueWithAllToken():
    allTokenUrl = 'https://price-api.crypto.com/price/v1/all-tokens'
    allTokenList = requests.get(url=allTokenUrl, params='', headers='').json()
    PriceEngineUrl = 'http://asta-crypto-token-price-engine.3ona.co/price/v1/latest'
    headers = {"Authorization": "Basic YXN0YV9mdWRfcHJpY2U6UU4sMmtReThURzJ5VyNELQ=="}
    priceEngineList = requests.get(url=PriceEngineUrl, params='', headers=headers).json()

    allTokenPrice = {}
    priceEngineTokenPrice = {}
    tokenSlug = {}
    # outOfListSlug = []
    theTokenUpatateTime = {}
    moreThanTheAcceptPercentageList = []
    for i in range(len(allTokenList)):
        tokenID = allTokenList[i]["id"]
        tokeSlug = allTokenList[i]["slug"]
        allTokePrice = allTokenList[i]["usd_price"]
        allTokenPrice[tokenID] = allTokePrice
        tokenSlug[tokenID] = tokeSlug

    for j in range(len(priceEngineList["data"])):
        tokenID = priceEngineList["data"][j]["id"]
        tokenPrice = priceEngineList["data"][j]["quote"]["USD"]["price"]
        priceEngineTokenPrice[tokenID] = tokenPrice
        tokenUpdateTime = priceEngineList["data"][j]["quote"]["USD"]["last_updated"]
        theTokenUpatateTime[tokenID] = tokenUpdateTime

    for key in allTokenPrice.keys():
        if key in priceEngineTokenPrice:
            theDifference = (float(allTokenPrice[key]) - float(priceEngineTokenPrice[key])) / float(
                priceEngineTokenPrice[key])
            if -0.04 < theDifference < 0.04:
                #写到文档里
                print("pass")
                continue
            else:
                # 写到文档里,id,slug,difference,update time
                print("fail")
                OutOfLimit = "{},slug:{},difference:{},tokenLastUpdateTime:{}" \
                    .format(key,tokenSlug[key],theDifference,theTokenUpatateTime[key])
                moreThanTheAcceptPercentageList.append(OutOfLimit)
    return moreThanTheAcceptPercentageList

def checkTheValueWithCoingekco():
    coingekcoUrl = 'https://api.coingecko.com/api/v3/coins/markets'
    parmas = {"vs_currency":"usd"}
    coingeckoList = requests.get(url=coingekcoUrl, params=parmas, headers='').json()
    PriceEngineUrl = 'http://asta-crypto-token-price-engine.3ona.co/price/v1/latest'
    headers = {"Authorization": "Basic YXN0YV9mdWRfcHJpY2U6UU4sMmtReThURzJ5VyNELQ=="}
    priceEngineList = requests.get(url=PriceEngineUrl, params='', headers=headers).json()

    coingekcoTokenPrice = {}
    priceEngineTokenPrice = {}
    tokenSlug = {}
    # outOfListSlug = []
    theTokenUpatateTime = {}
    moreThanTheAcceptPercentageList = []

    for i in range(len(coingeckoList)):
        tokeSlug = coingeckoList[i]["id"]
        gekcotokePrice = coingeckoList[i]["current_price"]
        tokeUpdateTime = coingeckoList[i]["last_updated"]
        coingekcoTokenPrice[tokeSlug] = gekcotokePrice
        tokenSlug[tokeSlug] = tokeUpdateTime

    for j in range(len(priceEngineList["data"])):
        # tokenID = priceEngineList["data"][j]["id"]
        engineSlug = priceEngineList["data"][j]["slug"]
        tokenPrice = priceEngineList["data"][j]["quote"]["USD"]["price"]
        priceEngineTokenPrice[engineSlug] = tokenPrice
        # priceEngineTokenPrice[tokenID] = engineSlug

    for key in coingekcoTokenPrice.keys():
        if key in priceEngineTokenPrice:
            theDifference = (float(coingekcoTokenPrice[key]) - float(priceEngineTokenPrice[key])) / float(
                priceEngineTokenPrice[key])
            if -0.04 < theDifference < 0.04:
                #写到文档里
                print("pass")
                continue
            else:
                # 写到文档里,id,slug,difference,update time
                print("fail")
                OutOfLimit = "{},slug:{},difference:{},tokenLastUpdateTime:{}" \
                    .format(key,tokenSlug[key],theDifference,theTokenUpatateTime[key])
                moreThanTheAcceptPercentageList.append(OutOfLimit)
    print(moreThanTheAcceptPercentageList)

if __name__ == "__main__":
    checkTheValueWithCMC()




