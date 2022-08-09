# https://www.acmicpc.net/problem/17089
import sys, collections
N, M = map(int, sys.stdin.readline().split())
FRIENDS = [[0] * 4001 for _ in range(4001)]
for _ in range(M):
    num1, num2 = map(int, sys.stdin.readline().split())
    FRIENDS[num1][num2] = 1
    FRIENDS[num2][num1] = 1

result = 1e9
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if FRIENDS[i][j]:
            for k in range(j + 1, N + 1):
                if FRIENDS[j][k] and FRIENDS[i][k]:
                    result = min(result, sum(FRIENDS[i]) + sum(FRIENDS[j]) + sum(FRIENDS[k]) - 6)

print(result) if result != 1e9 else print(-1)
