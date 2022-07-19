from toolstouse.time_handle import timeStamp
import time

import allure
import pytest
import os
from common.compare_token import CompareToken
from config.global_variables import *

Com = CompareToken()

@pytest.mark.tokenpricecomparison
@allure.feature("token price comparison module")
class TestComparison:

    @allure.story("test tokens'price With CMC")
    @allure.title("token price comparison with CMC")
    @pytest.mark.cmc
    def test_CMC(self):
        Com.checkTheValueWithCMC()
        time.sleep(15)
        with open(cmctxtPath, "rb") as f:
            context = f.read()
            allure.attach(context, "outOfLimitTokenCompareWithCMC.txt", attachment_type=allure.attachment_type.TEXT)

    # @allure.story("testWithAllToken")
    # @allure.title("token price with all tokens")
    # @pytest.mark.alltoken
    # @pytest.mark.skip
    # def test_allToken(self):
    #     Com.checkTheValueWithAllToken()
    #     with open(alltokentxtPath, "rb") as f:
    #         context = f.read()
    #         allure.attach(context, "outOfLimitTokenCompareWithAllToken.txt", attachment_type=allure.attachment_type.TEXT)

    @allure.story("testWithCoingecko")
    @allure.title("token price with coingecko")
    @pytest.mark.coingecko
    def test_Coingecko(self):
        Com.checkTheValueWithCoinGecko()
        time.sleep(15)
        with open(coingeckotxtPath, "rb") as f:
            context = f.read()
            allure.attach(context, "outOfLimitTokenCompareWithCoingecko.txt", attachment_type=allure.attachment_type.TEXT)


if __name__ == '__main__':
    reportName = timeStamp().str_time()
    #命令行
    os.system(
        f"python3 -m pytest comparison_test.py::TestComparison::test_CMC --count=1 --alluredir={theAllureDirPath} "
        f"--clean-alluredir")
    os.system(f'allure generate -c -o {theHtmlDirPath}%s {theAllureDirPath}' % reportName)
    os.system(f'allure serve {theAllureDirPath}')
    time.sleep(15)


