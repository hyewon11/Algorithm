# https://www.acmicpc.net/problem/1520
# dp
import sys
M, N = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]
def dfs(r, c):
    if r == M - 1 and c == N - 1:
        return 1
    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0
    for nr, nc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + nr, c + nc
        if 0 <= nr < M and 0 <= nc < N and MAP[nr][nc] < MAP[r][c]:
            dp[r][c] += dfs(nr, nc)
    return dp[r][c]

dfs(0, 0)
print(dfs(0, 0))
