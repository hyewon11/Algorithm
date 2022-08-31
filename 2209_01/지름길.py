# https://www.acmicpc.net/problem/1446

import sys, collections
N, D = map(int, sys.stdin.readline().split())
ROADS = collections.defaultdict(list)
for _ in range(N):
    start, end, length = map(int, sys.stdin.readline().split())
    ROADS[start].append((end, length))

dp = [1e9] * 10001
dp[0] = 0
for d in range(D):
    dp[d + 1] = min(dp[d] + 1, dp[d + 1])
    if ROADS[d]:
        for end, length in ROADS[d]:
            dp[end] = min(dp[end], dp[d] + length)

print(dp[D])
