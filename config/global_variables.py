import os

path = os.path.dirname(os.path.dirname(__file__))
theAllureDirPath = os.path.join(path + "/report/allure_report")
theHtmlDirPath = os.path.join(path + "/report/html_report/")
theResultDirPath = os.path.join(path + "/result")
testcases1Path = os.path.join(path + "/testcase/comparison_test.py")
cmctxtPath = os.path.join(path + "/result/outOfLimitTokenCompareWithCMC.txt")
alltokentxtPath = os.path.join(path + "/result/outOfLimitTokenCompareWithAllToken.txt")
coingeckotxtPath = os.path.join(path + "/result/outOfLimitTokenCompareWithCoingecko.txt")

if __name__ == "__main__":
    print(alltokentxtPath)