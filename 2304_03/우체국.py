# https://www.acmicpc.net/problem/2141
# Greedy -> 모두 순회하면 시간초과 발생
import sys
N = int(sys.stdin.readline())
VILLAGES = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

total = 0
for i in range(N):
    total += VILLAGES[i][1]

VILLAGES.sort()
cnt = 0
for i in range(N):
    cnt += VILLAGES[i][1]
    if cnt >= total / 2:
        print(VILLAGES[i][0])
        break
