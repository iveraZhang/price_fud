import os
from common.get_price import *
from tools.log_handle import ConsoleLogger
from tools.config_handle import *

log = ConsoleLogger()

class CompareToken:
    def __init__(self,num):
        # 选择与哪个环境进行对比，1 cmc  2 alltoken  3 coingecko
        if num == 1:
            log.info("choose CMC to compare")
            self.func = getCMCPrice()
        elif num == 2:
            log.info("choose alltokens to compare")
            self.func = getAllTokenPrice()
        elif num == 3:
            log.info("choose coingecko to compare")
            self.func = getCoingeckoPrice()
        else:
            log.info("wrong choice,please input right number"
                     "for 1 CMC, 2 Alltoken, 3 Coingecko")

    def campareToken(self):
        oneRun = []
        tokenId1 = []
        tokenId2 = []
        for i in getPriceEnginePrice()[0].keys():
            tokenId1.append(i)
        for j in self.func[0].keys():
            tokenId2.append(j)
        commonId = list(set(tokenId1) & set(tokenId2))
        for id in commonId:
            theDifference = (float(self.func[0][id]) - float(getPriceEnginePrice()[0][id])) / float(
                getPriceEnginePrice()[0][id])
            rate = readConfig("differential_rate","differential_rate")
            if -float(rate) < theDifference < float(rate):
                log.info(id)
                continue
            else:
                theDifferenceAndItsUpdateTime = "{},slug:{},difference:{},tokenLastUpdateTime:{}" \
                    .format(id, getPriceEnginePrice()[2][id], theDifference, getPriceEnginePrice()[1][id])
                oneRun.append(theDifferenceAndItsUpdateTime)
        saveDataFilePath = os.path.dirname(__file__) + "/../result/outOfLimitToken.txt"
        if oneRun == []:
            saveDataFile = open(saveDataFilePath, "a")
            saveDataFile.write("\npass")
            saveDataFile.close()
            return 0

        else:
            saveDataFile = open(saveDataFilePath, "a")
            saveDataFile.write(
                "\n{}".format(oneRun))
            saveDataFile.close()
        return oneRun


if __name__ == '__main__':
    CompareToken(1).campareToken()

