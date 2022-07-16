# https://www.acmicpc.net/problem/4485
# 12:54 - 1:07 (13 m)

import sys, collections
cnt = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    CAVE = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    q = collections.deque()
    q.append((0, 0))
    visit = [[1e9] * N for _ in range(N)]
    visit[0][0] = CAVE[0][0]
    while q:
        r, c = q.popleft()
        for nr, nc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + nr, c + nc
            if 0 <= nr < N and 0 <= nc < N and visit[r][c] + CAVE[nr][nc] < visit[nr][nc]:
                q.append((nr, nc))
                visit[nr][nc] = visit[r][c] + CAVE[nr][nc]

    print("Problem " + str(cnt) +": "+str(visit[N - 1][N - 1]))
    cnt += 1
