import math
import time

class Timestamp:
    def get_now_timestamp_miliseconds(self):
        timestamp =  math.trunc(time.time())*1000
        print(timestamp)
        return timestamp