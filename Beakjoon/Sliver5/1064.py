import sys
import math

INF = int(1e9)
# 평행 사변형이 만들어진다면 3개의 경우의 수가 존재한다.
# 평생 사변형이 만들어지지 않는 경우는 3점이 한 직선상에 있는 경우이다
# 따라서 (a, b), (b, c)의 기울기를 비교 후 일치 하다면 -1을 반환
# 일치하지 않는다면 3점을 이은 선분 3개의 길이를 구하여 가장 큰 쌍과 가장 작은 쌍을 이용하여 가장 큰 둘레 길이와 가장 작은 둘레 길이를 구한다.

def lineLength(Xa, Xb, Ya, Yb):
    return math.sqrt(math.pow(Xa - Xb, 2) + math.pow(Ya - Yb, 2))

input = sys.stdin.readline

Xa, Ya, Xb, Yb, Xc, Yc = map(int, input().split())

if Xa - Xb != 0:
    gradientAB = (Ya - Yb) / (Xa - Xb)
else:
    gradientAB = INF

if Xb - Xc != 0:
    gradientBC = (Yb - Yc) / (Xb - Xc)
else:
    gradientBC = INF

if gradientAB == gradientBC:
    print(-1.0)
else:
    lineAB = lineLength(Xa, Xb, Ya, Yb)
    lineBC = lineLength(Xb, Xc, Yb, Yc)
    lineCA = lineLength(Xc, Xa, Yc, Ya)

    length = [lineAB, lineBC, lineCA]
    length.sort()

    maxSum = (length[2] + length[1]) * 2
    minSum = (length[0] + length[1]) * 2

    print(maxSum - minSum)