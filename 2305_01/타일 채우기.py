# https://www.acmicpc.net/problem/2133
# dp
import sys
N = int(sys.stdin.readline())
dp = [0] * 31
dp[0], dp[2] = 1, 3

for i in range(3, N + 1):
    if i % 2 == 0:
        dp[i] = dp[2] * dp[i - 2]
        for j in range(4, N + 1):
            if j % 2 == 0:
                dp[i] += 2 * dp[i - j]

print(dp[N])
