# https://www.acmicpc.net/problem/4811
# 카탈란 수 사용
import math, sys
def catalan(n):
    return math.factorial(2 * n) // (math.factorial(n) * math.factorial(n + 1))

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    print(catalan(N))
