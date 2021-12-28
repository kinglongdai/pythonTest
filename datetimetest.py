import time

def get_now(year: int, month: int, day: int):
   return time.strftime("%Y-%m-%d",time.localtime())




print(get_now(2021, 12, 1))

