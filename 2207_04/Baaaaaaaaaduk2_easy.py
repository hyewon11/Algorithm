# 3h
import sys, collections
def count_stone():
    stones = 0
    visit = [[False] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if BOARD[r][c] == 2 and not visit[r][c]:
                cnt, is_zero = 0, True
                q = collections.deque()
                q.append((r, c))
                visit[r][c] = True
                while q:
                    cur_r, cur_c = q.popleft()
                    cnt += 1
                    for i in range(4):
                        nr, nc = cur_r + NR[i], cur_c + NC[i]
                        if 0 <= nr < N and 0 <= nc < M:
                            if BOARD[nr][nc] == 0:
                                is_zero = False
                            if BOARD[nr][nc] == 2 and not visit[nr][nc]:
                                q.append((nr, nc))
                                visit[nr][nc] = True
                if is_zero:
                    stones += cnt
    return stones
N, M = map(int, sys.stdin.readline().split())
BOARD = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

NR, NC = [0, 0, 1, -1], [1, -1, 0, 0]
result = 0
blank_spaces = []
for r in range(N):
    for c in range(M):
        if BOARD[r][c] == 0:
            blank_spaces.append((r, c))

for i in range(len(blank_spaces)):
    for j in range(len(blank_spaces)):
        (r1, c1), (r2, c2) = blank_spaces[i], blank_spaces[j]
        BOARD[r1][c1], BOARD[r2][c2] = 1, 1
        result = max(count_stone(), result)
        BOARD[r1][c1], BOARD[r2][c2] = 0, 0
print(result)
