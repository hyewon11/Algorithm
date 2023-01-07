# https://www.acmicpc.net/problem/1103
import sys
N, M = map(int, sys.stdin.readline().split())
X = [list(sys.stdin.readline().strip()) for _ in range(N)]

visit = [[False] * (M + 1) for _ in range(N + 1)]
dp = [[0] * (M + 1) for _ in range(N + 1)]
result = -1

def dfs(r, c, cnt):
    global result
    n = int(X[r][c])
    result = max(result, cnt)
    
    for nr, nc in [(0, -n), (0, n), (-n, 0), (n, 0)]:
        nr, nc = r + nr, c + nc
        if 0 <= nr < N and 0 <= nc < M and dp[nr][nc] < cnt + 1:
            if X[nr][nc] == 'H':
                continue
            if visit[nr][nc]:
                print(-1)
                sys.exit()
            
            dp[nr][nc] = cnt + 1 
            visit[nr][nc] = True
            dfs(nr, nc, cnt + 1)
            visit[nr][nc] = False

visit[0][0] = True
dfs(0, 0, 0)
print(result + 1)
