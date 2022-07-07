import os

path = os.path.dirname(os.path.dirname(__file__))
theAllureDirPath = os.path.join(path + "/report/allure_report")
theHtmlDirPath = os.path.join(path + "/report/html_report/")
testcases1Path = os.path.join(path + "/testcase/test_cmc.py")
testcases2Path = os.path.join(path + "/testcase/test_all_token.py")
testcases3Path = os.path.join(path + "/testcase/test_coingekco.py")

if __name__ == "__main__":
    print(theAllureDirPath)