# https://www.acmicpc.net/problem/11501
# Greedy

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    PRICES = list(map(int, sys.stdin.readline().split()))
    
    result, max_p = 0, PRICES[-1]
    for i in range(N - 2, -1, -1):
        if max_p < PRICES[i]:
            max_p = PRICES[i]
        else:
            result += max_p - PRICES[i]
    print(result)
