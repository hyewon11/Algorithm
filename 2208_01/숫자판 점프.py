# https://www.acmicpc.net/problem/2210
import sys, collections
def dfs(r, c, move, num):
    global cnt
    if move == 5:
        if digits[num] == 0:
            digits[num] = 1
            cnt += 1
        return
    for nr, nc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + nr, c + nc
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, move + 1, num + str(BOARD[nr][nc]))

BOARD = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
digits = collections.defaultdict(int)
cnt = 0
for r in range(5):
    for c in range(5):
        dfs(r, c, 0, str(BOARD[r][c]))
print(cnt)
