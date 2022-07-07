from tools.time_handle import timeStamp
import time

import allure
import pytest
import os
from common.compare_token import CompareToken
from config.global_variables import *

@pytest.mark.tokenpricecomparison
@allure.feature("token price comparison module")
class TestComparison:

    @allure.story("test tokens'price With CMC")
    @allure.title("token price comparison with CMC")
    def test_CMC(self):
        CompareToken(1).campareToken()
        # pass
        with open("/Users/verazhang/Desktop/fud/result/outOfLimitToken.txt", "rb") as f:
            context = f.read()
            allure.attach(context, "outOfLimitToken.txt", attachment_type=allure.attachment_type.TEXT)

    @allure.story("testWithAllToken")
    @allure.title("token price with all tokens")
    def test_allToken(self):
        pass
        # CompareToken(2).campareToken()

    @allure.story("testWithCoingecko")
    @allure.title("token price with coingecko")
    def test_Coingecko(self):
        pass
        # CompareToken(3).campareToken()


if __name__ == '__main__':
    reportName = timeStamp().str_time()
    #命令行
    os.system(
        f"python3 -m pytest comparison_test.py::TestComparison::test_CMC --count=30 --alluredir={theAllureDirPath}"
    )
        # f"--clean -alluredir")
    os.system(f'allure generate -c -o {theHtmlDirPath}%s {theAllureDirPath}' % reportName)
    os.system(f'allure serve {theAllureDirPath}')
    time.sleep(15)


