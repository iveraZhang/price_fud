# coding = utf-8
#!/usr/bin/python3
import sys
sys.path.append("..")

import time
import os

from config.global_variables import theHtmlDirPath, theAllureDirPath
from toolstouse.config_handle import readConfig
from testcase.comparison_test import TestComparison
from toolstouse.log_handle import ConsoleLogger
from toolstouse.time_handle import timeStamp
from config.global_variables import *


log = ConsoleLogger()
reportName = timeStamp().str_time()

file = open(cmctxtPath, 'w').close()
file1 = open(alltokentxtPath, 'w').close()
file2 = open(coingeckotxtPath, 'w').close()

os.system(f"python3 -m pytest {testcases1Path} --count=10 --alluredir={theAllureDirPath} --clean-alluredir")
os.system(f'allure generate -c -o {theHtmlDirPath}%s {theAllureDirPath}' % reportName)
os.system(f'allure serve {theAllureDirPath}')
time.sleep(15)


