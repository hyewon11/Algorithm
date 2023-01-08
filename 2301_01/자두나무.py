# https://www.acmicpc.net/problem/2240
import sys
T, W = map(int, sys.stdin.readline().split())
TREE = list(int(sys.stdin.readline().strip()) for _ in range(T))

dp = [[[0] * 2 for _ in range(T + 1)] for _ in range(W + 2)]
for t in range(1, T + 1):
    loc = TREE[t - 1]
    for w in range(1, W + 2):
        if loc == 1:
            dp[w][t][0] = max(dp[w][t - 1][0] + 1, dp[w - 1][t - 1][1] + 1)
            dp[w][t][1] = max(dp[w][t - 1][1], dp[w - 1][t - 1][0])
        else:
            if t == 1 and w == 1:
                continue
            dp[w][t][0] = max(dp[w][t - 1][0], dp[w - 1][t - 1][1])
            dp[w][t][1] = max(dp[w][t - 1][1] + 1, dp[w - 1][t - 1][0] + 1)

result = 0
for i in range(1, W + 2):
    for j in range(2):
        result = max(result, dp[i][T][j])
print(result)
