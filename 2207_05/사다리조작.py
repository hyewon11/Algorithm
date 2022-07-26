# (시간 초과)
# https://www.acmicpc.net/problem/15684
import sys
N, M, H = map(int, sys.stdin.readline().split())
WIDTH_LINES = [[0] * (H + 1) for _ in range(N + 1)] # 세로, 가로
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    WIDTH_LINES[b][a], WIDTH_LINES[b + 1][a] = b + 1, b

def check():
    for start in range(1, N + 1):
        r = start
        for c in range(1, H + 1):
            r = WIDTH_LINES[r][c] if WIDTH_LINES[r][c] else r
        if r != start:
            return False
    return True

result = 1e9
def dfs(idx_point, cnt):
    global result
    if cnt > 3:
        return
    if idx_point >= len(candidate_points):
        if check():
            result = min(result, cnt)
        return

    r, c = candidate_points[idx_point][0], candidate_points[idx_point][1]
    dfs(idx_point + 1, cnt)
    if not WIDTH_LINES[r][c]:
        WIDTH_LINES[r][c], WIDTH_LINES[r + 1][c] = r + 1, r
        dfs(idx_point + 1, cnt + 1)
        WIDTH_LINES[r][c], WIDTH_LINES[r + 1][c] = 0, 0

candidate_points = [(r, c) for r in range(1, N) for c in range(1, H + 1) if not WIDTH_LINES[r][c] and not WIDTH_LINES[r + 1][c]]
dfs(0, 0)
print(result) if result != 1e9 else print(-1)
