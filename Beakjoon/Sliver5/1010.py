import sys

input = sys.stdin.readline

number = int(input())
dp = [[0 for _ in range(31)] for _ in range(31)]

def Combine(n, m):
    if dp[m][n]:
        return dp[m][n]
    if n == m or m == 0:
        return 1
    dp[m][n] = Combine(n - 1, m) + Combine(n - 1, m - 1)
    return dp[m][n]

for i in range(number):
    n, m = map(int, input().split())
    print(Combine(m, n))