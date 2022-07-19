import ssl
import sys
from common.get_price import *
from toolstouse.log_handle import ConsoleLogger
from toolstouse.config_handle import *
from config.global_variables import *

log = ConsoleLogger()

class CompareToken(object):
    def __init__(self):
        self.priceEngineUrl = readConfig("env", "url")
        self.engineKey = readConfig("env", "engineKey")
        self.allTokensUrl = readConfig("unipath", "allTokens")
        self.cmcTokenUrl = readConfig("unipath", "cmcToken")
        self.coingeckoUrl = readConfig("unipath", "coingecko")
        self.rate = readConfig("differential_rate", "differential_rate")
        log.info(self.priceEngineUrl)
        log.info(self.engineKey)
    def checkTheValueWithCMC(self):
        header1 = {}
        header2 = {}
        params1 = {}
        params1["limit"]=5000
        header1["X-CMC_PRO_API_KEY"]=readConfig("cmc_key","CMCApiKey")
        header2["Authorization"]=self.engineKey
        theStatusFromTheCMCApi = requests.get(url=self.cmcTokenUrl, params=params1, headers=header1，verify=False)
        if theStatusFromTheCMCApi.status_code == 200:
            log.info(f"CMC's status_code:\r\n{theStatusFromTheCMCApi.status_code},get data from CMC success")
            theListFromTheCMCApi = theStatusFromTheCMCApi.json()["data"]
            thelistFromThePriceEngineApi = requests.get(url=self.priceEngineUrl, params='', headers=header2)
            thestatusFromThePriceEngineApi = thelistFromThePriceEngineApi.status_code
            try:
                if thestatusFromThePriceEngineApi == 200:
                    log.info(f"PriceEngineApi's status_code:\r\n{theStatusFromTheCMCApi.status_code},get data from PriceEngineApi success")
                    theDataFromThePriceEngineApi = thelistFromThePriceEngineApi.json()[ "data"]
                    theListFromTheCMCPrice = {}
                    theListFromThePriceEnginePrice = {}
                    outOfListSlug = []
                    theTokenUpatateTime = {}
                    moreThanTheAcceptPercentageList = []
                    for i in range(len(theDataFromThePriceEngineApi)):
                        tokenID = theDataFromThePriceEngineApi[i]["id"]
                        tokenPrice = theDataFromThePriceEngineApi[i]["quote"]["USD"]["price"]
                        tokenUpdateTime = theDataFromThePriceEngineApi[i]["quote"]["USD"]["last_updated"]
                        theListFromThePriceEnginePrice[tokenID] = tokenPrice
                        theTokenUpatateTime[tokenID] = tokenUpdateTime
                    for j in range(len(theListFromTheCMCApi)):
                        tokenID = theListFromTheCMCApi[j]["id"]
                        tokenPrice = theListFromTheCMCApi[j]["quote"]["USD"]["price"]
                        theListFromTheCMCPrice[tokenID] = tokenPrice
                    for key in theListFromThePriceEnginePrice.keys():
                        if key in theListFromTheCMCPrice:
                            theDifference = (float(theListFromThePriceEnginePrice[key]) - float(theListFromTheCMCPrice[key])) / float(
                                theListFromTheCMCPrice[key])
                            log.info(f"id:{key},the difference price is {theDifference}")

                            if -(float(self.rate)) < theDifference < float(self.rate):
                                continue
                            else:
                                theDifferenceAndItsUpdateTime = "{}:{},tokenLastUpdateTime:{}" \
                                    .format(key, theDifference, theTokenUpatateTime[key])
                                moreThanTheAcceptPercentageList.append(theDifferenceAndItsUpdateTime)
                                log.error(f"id:{key},the difference price is {theDifference}")
                        else:
                            outOfListSlug.append(key)
                            continue

                    if moreThanTheAcceptPercentageList == [] and outOfListSlug == []:
                        saveDataFilePath = os.path.join(theResultDirPath,"outOfLimitTokenCompareWithCMC.txt")
                        saveDataFile = open(saveDataFilePath, "a")
                        saveDataFile.write("\npass")
                        saveDataFile.close()
                        return 0
                    else:
                        saveDataFilePath = os.path.join(theResultDirPath, "outOfLimitTokenCompareWithCMC.txt")
                        saveDataFile = open(saveDataFilePath, "a")
                        if outOfListSlug != []:
                            saveDataFile.write(
                                "\n{} theSlugNotInCMC:{}".format(moreThanTheAcceptPercentageList, outOfListSlug))
                        else:
                            saveDataFile.write("\n{}".format(moreThanTheAcceptPercentageList))
                        saveDataFile.close()
                        return moreThanTheAcceptPercentageList, outOfListSlug
                else:
                    log.error(f"fail to get data from price engine")
                    sys.exit(1)
            except ssl.SSLError as e:
                log.error(f"ssl.SSLEOFError:{e}")
                sys.exit(1)
        else:
            log.error(f"fail to get data from cmc,msg{theStatusFromTheCMCApi.json()}")
            sys.exit(1)

    def checkTheValueWithAllToken(self):
        header2 = {}
        header2["Authorization"]=self.engineKey
        theListFromThePriceEngineApi = requests.get(url=self.priceEngineUrl, params='', headers=header2).json()["data"]
        theListFromTheAllTokenApi = requests.get(url=self.allTokensUrl, params='', headers='').json()
        theListFromThePriceEnginePrice = {}
        theListFromTheAllTokenPrice = {}
        outOfListSlug = []
        theTokenUpatateTime = {}
        moreThanTheAcceptPercentageList = []

        for i in range(len(theListFromThePriceEngineApi)):
            tokenID = theListFromThePriceEngineApi[i]["id"]
            tokenPrice = theListFromThePriceEngineApi[i]["quote"]["USD"]["price"]
            tokenUpdateTime = theListFromThePriceEngineApi[i]["quote"]["USD"]["last_updated"]
            theListFromThePriceEnginePrice[tokenID] = tokenPrice
            theTokenUpatateTime[tokenID] = tokenUpdateTime
        for j in range(len(theListFromTheAllTokenApi)):
            tokenName = theListFromTheAllTokenApi[j]["slug"]
            tokenPrice = theListFromTheAllTokenApi[j]["usd_price"]
            theListFromTheAllTokenPrice[tokenName] = tokenPrice

        for key in theListFromThePriceEnginePrice.keys():
            if key in theListFromTheAllTokenPrice:
                theDifference = (float(theListFromThePriceEnginePrice[key]) - float(theListFromTheAllTokenPrice[key])) / float(
                    theListFromTheAllTokenPrice[key])
                if -(float(self.rate)) < theDifference < float(self.rate):
                    continue
                else:
                    theDifferenceAndItsUpdateTime = "{}:{},tokenLastUpdateTime:{}" \
                        .format(key, theDifference, theTokenUpatateTime[key])
                    moreThanTheAcceptPercentageList.append(theDifferenceAndItsUpdateTime)
            else:
                outOfListSlug.append(key)
                continue

        if moreThanTheAcceptPercentageList == [] and outOfListSlug == []:
            saveDataFilePath = os.path.join(theResultDirPath, "outOfLimitTokenCompareWithAllToken.txt")
            saveDataFile = open(saveDataFilePath, "a")
            saveDataFile.write("\npass")
            saveDataFile.close()
            return 0
        else:
            saveDataFilePath = os.path.join(theResultDirPath, "outOfLimitTokenCompareWithAllToken.txt")
            saveDataFile = open(saveDataFilePath, "a")
            if outOfListSlug != []:
                saveDataFile.write(
                    "\n{}  theSlugNotInAllToken:{}".format(moreThanTheAcceptPercentageList,
                                                           outOfListSlug))
            else:
                saveDataFile.write("\n{}".format(moreThanTheAcceptPercentageList))
            saveDataFile.close()
            return moreThanTheAcceptPercentageList


    def checkTheValueWithCoinGecko(self):
        header2 = {}
        params1 = {}
        params1["vs_currency"] = "usd"
        header2["Authorization"]=self.engineKey
        thelistFromThePriceEngineApi = requests.get(url=self.priceEngineUrl, params='', headers=header2)
        if thelistFromThePriceEngineApi.status_code == 200:
            log.info(
                f"PriceEngineApi's status_code:\r\n{thelistFromThePriceEngineApi.status_code},get data from PriceEngineApi success")
            theDataFromThePriceEngineApi =thelistFromThePriceEngineApi.json()["data"]
            theListFromTheCoingeckoApi = requests.get(url=self.coingeckoUrl, params=params1, headers='')
            try:
                if theListFromTheCoingeckoApi.status_code == 200:
                    log.info(
                        f"coingecko's status_code:\r\n{thelistFromThePriceEngineApi.status_code},get data from coingecko success")
                    theDataFromTheCoingeckoApi = theListFromTheCoingeckoApi.json()
                    theListFromTheCoingeckoPrice = {}
                    theListFromThePriceEnginePrice = {}
                    outOfListToken = []
                    theTokenUpdateTime = {}
                    moreThanTheAcceptPercentageList = []
                    for i in range(len(theDataFromThePriceEngineApi)):
                        tokenSymbol = theDataFromThePriceEngineApi[i]["symbol"]
                        tokenPrice = theDataFromThePriceEngineApi[i]["quote"]["USD"]["price"]
                        tokenUpdateTime = theDataFromThePriceEngineApi[i]["quote"]["USD"]["last_updated"]
                        theListFromThePriceEnginePrice[tokenSymbol] = tokenPrice
                        theTokenUpdateTime[tokenSymbol] = tokenUpdateTime
                    for j in range(len(theDataFromTheCoingeckoApi)):
                        tokenSymbol = theDataFromTheCoingeckoApi[j]["symbol"]
                        tokenPrice = theDataFromTheCoingeckoApi[j]["current_price"]
                        theListFromTheCoingeckoPrice[tokenSymbol] = tokenPrice
                    for key in theListFromThePriceEnginePrice.keys():
                        theSecondApiKey = str.lower(key)
                        if theSecondApiKey in theListFromTheCoingeckoPrice:
                            theDifference = (float(theListFromThePriceEnginePrice[key]) - float(
                                theListFromTheCoingeckoPrice[theSecondApiKey])) / float(
                                theListFromTheCoingeckoPrice[theSecondApiKey])
                            log.info(f"id:{key},the difference price is {theDifference}")
                            if -(float(self.rate)) < theDifference < float(self.rate):
                                continue
                            else:
                                theDifferenceAndItsUpdateTime = "{}:{},tokenLastUpdateTime:{}" \
                                    .format(key, theDifference, theTokenUpdateTime[key])
                                moreThanTheAcceptPercentageList.append(theDifferenceAndItsUpdateTime)
                            log.info(f"moreThanTheAcceptPercentageList:{moreThanTheAcceptPercentageList}")
                            log.error(f"id:{key},the difference price is {theDifference}")
                        else:
                            continue

                    if moreThanTheAcceptPercentageList == []:
                        saveDataFilePath = os.path.join(theResultDirPath, "outOfLimitTokenCompareWithCoingecko.txt")
                        saveDataFile = open(saveDataFilePath, "a")
                        saveDataFile.write("\npass")
                        saveDataFile.close()
                        return 0
                    else:
                        saveDataFilePath = os.path.join(theResultDirPath, "outOfLimitTokenCompareWithCoingecko.txt")
                        saveDataFile = open(saveDataFilePath, "a")
                        if outOfListToken != []:
                            saveDataFile.write(
                                "\n{} theOutOfToken:{}".format(moreThanTheAcceptPercentageList, outOfListToken))
                        else:
                            saveDataFile.write("\n{}".format(moreThanTheAcceptPercentageList))
                        saveDataFile.close()
                        return moreThanTheAcceptPercentageList, outOfListToken
                else:
                    log.error(f"fail to get data from coingecko,msg:{theListFromTheCoingeckoApi}")
                    sys.exit(1)
            except ssl.SSLEOFError as e:
                log.error(f"ssl.SSLEOFError:{e}")
                sys.exit(1)
        else:
            log.error(f"fail to get data from price engine,msg:{thelistFromThePriceEngineApi}")
            sys.exit(1)


if __name__ == '__main__':
    # res = CompareToken().checkTheValueWithCoinGecko()
    # print(CompareToken().checkTheValueWithCoinGecko())
    # print(CompareToken().checkTheValueWithAllToken())

    print(CompareToken().checkTheValueWithCMC())


