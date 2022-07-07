import time
import datetime


class timeStamp:
    def __init__(self):
        self.time = time.time()

    def raw_time(self):
        raw_time = self.time
        return raw_time  # 原始时间数据

    def sec_time(self):
        sec_time = int(self.time)
        return sec_time  # 秒级时间戳

    def ms_time(self):
        ms_time = int(round(self.time*1000))
        return ms_time  # 毫秒级时间戳

    def mic_time(self):
        mic_time = int(round(self.time*1000000))
        return mic_time  # 微秒级时间戳

    def str_time(self):
        str_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        return str_time  # 年月日时分秒时间格式

if __name__ =="__main__":
    print(timeStamp().str_time())