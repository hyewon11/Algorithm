# https://www.acmicpc.net/problem/1890
# dp
import sys
N = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[-1] * N for _ in range(N)]
def dfs(r, c):
    if r == N-1 and c== N-1:
        return 1
    if dp[r][c] != -1:
        return dp[r][c]
    
    dp[r][c] = 0
    if MAP[r][c] != 0:
        for nr, nc in [(0, 1), (1, 0)]:
            nr, nc = r + nr * MAP[r][c], c + nc * MAP[r][c]
            if 0 <= nr < N and 0 <= nc < N:
                dp[r][c] += dfs(nr, nc)
    return dp[r][c]

print(dfs(0, 0))
