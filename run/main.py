# coding = utf-8
import datetime
import os
import time
import allure
import pytest

from tools.log_handle import ConsoleLogger
import requests
import os
import shutil
from tools.config_handle import readConfig

log = ConsoleLogger()
# if __name__ == "__main__":
#     theAllureDirPath = os.path.abspath(__file__) + "/../report/allure_report"
#     theHtmlDirPath = os.path.abspath(__file__) + "/../report/html_report"
#     testcases1Path = os.path.abspath(__file__) + "/../testcase/test_cmc.py"
#     testcases2Path = os.path.abspath(__file__) + "/../testcase/test_all_token.py"
#     testcases3Path = os.path.abspath(__file__) + "/../testcase/test_coingekco.py"
#     test = os.path.abspath(__file__) + "/../testcase/comparison_test.py"
#
#     for i in range(1):
#         # shutil.rmtree("{}".format(logpath))
#         # os.mkdir("{}".format(logpath))
#         # shutil.rmtree("{}".format(reportPath))
#         # pytest.main()
#         reportName = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
#         pytest.main([test, '-s', '--alluredir', f'{theAllureDirPath}'])
#         os.system(f'allure generate -c -o {theHtmlDirPath}%s {theAllureDirPath}' % reportName)
#         os.system(f'allure serve {theAllureDirPath}')
#         time.sleep(15)
