# https://www.acmicpc.net/problem/1987
import sys
R, C = map(int, sys.stdin.readline().split())
BOARD = [list(sys.stdin.readline().strip()) for _ in range(R)]

for r in range(R):
    for c in range(C):
        BOARD[r][c] = ord(BOARD[r][c]) - 65

NR, NC = [0, 0, 1, -1], [1, -1, 0, 0]
alphabets = [False] * 26
result = 0

def dfs(r, c, move):
    global result
    result = max(result, move)
    for i in range(4):
        nr, nc = r + NR[i], c + NC[i]
        if 0 <= nr < R and 0 <= nc < C and alphabets[BOARD[nr][nc]] == 0:
            alphabets[BOARD[nr][nc]] = True
            dfs(nr, nc, move + 1)
            alphabets[BOARD[nr][nc]] = False

alphabets[BOARD[0][0]] = True
dfs(0, 0, 1)
print(result)
