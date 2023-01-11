# https://www.acmicpc.net/problem/17404
import sys
N = int(sys.stdin.readline())
COST = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[[1e9] * 3 for _ in range(N)] for _ in range(3)]
result = 1e9
for start in range(3):
    for i in range(3):
        if start != i:
            dp[start][1][i] = COST[0][start] + COST[1][i]
    for i in range(2, N - 1):
        dp[start][i][0] = min(dp[start][i - 1][1], dp[start][i - 1][2]) + COST[i][0]
        dp[start][i][1] = min(dp[start][i - 1][0], dp[start][i - 1][2]) + COST[i][1]
        dp[start][i][2] = min(dp[start][i - 1][1], dp[start][i - 1][0]) + COST[i][2]
    for i in range(3):
        if i != start:
            if i == 0:
                dp[start][N - 1][0] = min(dp[start][N - 2][2], dp[start][N - 2][1]) + COST[N - 1][0]
            elif i == 1:
                dp[start][N - 1][1] = min(dp[start][N - 2][0], dp[start][N - 2][2]) + COST[N - 1][1]
            else:
                dp[start][N - 1][2] = min(dp[start][N - 2][1], dp[start][N - 2][0]) + COST[N - 1][2]
    result = min(result, dp[start][N - 1][0], dp[start][N - 1][1], dp[start][N - 1][2])
print(result)
