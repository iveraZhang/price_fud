from tools.log_handle import ConsoleLogger
import requests
import os
from tools.config_handle import readConfig

log = ConsoleLogger()
configPath = os.path.abspath(__file__)+"/../config/env.ini"

def getCMCPrice():
    # 得到CMC token的id,name,价钱，updatetime
    # 100token
    priceResult = {}
    tokenSlug = {}
    tokenUpdateTime = {}
    url = readConfig("path","cmcToken")
    #https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest
    log.info(f"CMC's URL：\r\n{url}")
    params = {"limit":"5000"}
    header = readConfig("cmc_key","CMCApiKey")
    headers = {"X-CMC_PRO_API_KEY": header}
    cmcList = requests.get(url=url, params=params, headers=headers).json()
    for i in range(len(cmcList["data"])):
        tokenID = cmcList["data"][i]["id"]
        # print(tokenID)
        tokeSlug = cmcList["data"][i]["slug"]
        tokenPrice = cmcList["data"][i]["quote"]["USD"]["price"]
        tokeUpdateTime = cmcList["data"][i]["quote"]["USD"]["last_updated"]
        priceResult[tokenID] = tokenPrice
        tokenUpdateTime[tokenID] = tokeUpdateTime
        tokenSlug[tokenID] = tokeSlug
    # #reture多个用元组方式组合
    return priceResult, tokenUpdateTime, tokenSlug


def getPriceEnginePrice():
    # 得到PriceEngine token的id,name,价钱，updatetime
    # 区分生产和测试环境
    # 195 token
    priceResult = {}
    tokenSlug = {}
    tokenUpdateTime = {}
    url = readConfig("path", "stagPriceEngine")
    header = readConfig("engine_key","stag")
    headers = {"Authorization": header}
    priceEngineList = requests.get(url=url, params='', headers=headers).json()
    for token in priceEngineList["data"]:
        tokenID = token["id"]
        tokeSlug = token["slug"]
        tokenPrice = token["quote"]["USD"]["price"]
        tokeUpdateTime = token["quote"]["USD"]["last_updated"]
        priceResult[tokenID] = tokenPrice
        tokenUpdateTime[tokenID] = tokeUpdateTime
        tokenSlug[tokenID] = tokeSlug
    return priceResult, tokenUpdateTime, tokenSlug

def getAllTokenPrice():
    # 得到AllToken的id,name,价钱，updatetime
    # 13394 token
    priceResult = {}
    tokenSlug = {}
    url = readConfig("path", "stagAllTokens")
    log.info(f"all token's URL：\r\n{url}")
    allTokenList = requests.get(url=url, params='', headers='').json()
    for token in allTokenList:
        tokenID = token["id"]
        tokeSlug = token["slug"]
        tokenPrice = token["usd_price"]
        priceResult[tokenID] = tokenPrice
        tokenSlug[tokenID] = tokeSlug
    return priceResult, tokenSlug

def getCoingeckoPrice():
    # 得到Coingecko的id,name,价钱，updatetime
    # {'id': '01coin', 'symbol': 'zoc', 'name': '01coin'}
    # 24500 token
    tokenSlug = {}
    tokenUpdateTime = {}
    url = readConfig("path", "coingecko")
    parmas = {"vs_currency":"usd"}
    log.info(f"all token's URL：\r\n{url}")
    allPriceList = requests.get(url=url, params=parmas, headers='').json()

    for i in range(len(allPriceList)):
        tokeSlug = allPriceList[i]["id"]
        tokePrice = allPriceList[i]["current_price"]
        tokeUpdateTime = allPriceList[i]["last_updated"]
        tokenSlug[tokeSlug] = tokePrice
        tokenUpdateTime[tokeSlug]=tokeUpdateTime
        #({'bitcoin': 19167.1,
    return tokenSlug, tokenUpdateTime

if __name__ == "__main__":
    # print(getCMCPrice())
    # print(getAllTokenPrice())
    print(getPriceEnginePrice())