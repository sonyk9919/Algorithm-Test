import sys
import datetime

input = sys.stdin.readline

nowYear, nowMonth, nowDay = map(int, input().split())
tarYear, tarMonth, tarDay = map(int, input().split())

n = datetime.datetime(nowYear, nowMonth, nowDay)
n_1000 = datetime.datetime(nowYear + 1000, nowMonth, nowDay)
t = datetime.datetime(tarYear, tarMonth, tarDay)

day_1000 = (n_1000 - n).days
day = (t - n).days

if day >= day_1000:
    print("gg")
else:
    print("D-{}".format(day))

