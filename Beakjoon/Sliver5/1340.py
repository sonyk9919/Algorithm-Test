import sys
import datetime as dt

input = sys.stdin.readline

nowTime = list(input().split())
nowTime[1] = nowTime[1][:-1]
nowTime[3] = nowTime[3].split(":")
totalOneYearToSec = 0

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

n = dt.datetime(int(nowTime[2]), month.index(nowTime[0]) + 1, int(nowTime[1]), int(nowTime[3][0]), int(nowTime[3][1]))
f = dt.datetime(int(nowTime[2]), 1, 1, 0, 0, 0)
diff = n - f

def isYoonYear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 > 0): return True
    return False

if (isYoonYear(int(nowTime[2]))):
    totalOneYearToSec = 366 * 24 * 60 * 60
else:
    totalOneYearToSec = 365 * 24 * 60 * 60

print(diff.total_seconds() / totalOneYearToSec * 100)
