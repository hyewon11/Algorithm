# https://www.acmicpc.net/problem/3197
import sys, collections
R, C = map(int, sys.stdin.readline().split())
LAKE = [list(sys.stdin.readline().strip()) for _ in range(R)]

NR = (0, 0, 1, -1)
NC = (1, -1, 0, 0)
swan_locations = []
q = collections.deque()
water_q = collections.deque()
visit = [[False] * (C + 1) for _ in range(R + 1)]
melt_visit = [[False] * (C + 1) for _ in range(R + 1)]

for r in range(R):
    for c in range(C):
        if LAKE[r][c] == 'L':
            LAKE[r][c] = '.'
            swan_locations.append((r, c))

        if LAKE[r][c] == 'X':
            for i in range(4):
                nr, nc = NR[i] + r, NC[i] + c
                if 0 <= nr < R and 0 <= nc < C and LAKE[nr][nc] != 'X':
                    water_q.append((r, c))
                    break


q.append(swan_locations[0])
visit[swan_locations[0][0]][swan_locations[0][1]] = True

day = 0
while True:
    # check to meet
    isStop = False
    next_q = collections.deque()
    while q:
        cur_r, cur_c = q.popleft()
        if cur_r == swan_locations[1][0] and cur_c == swan_locations[1][1]:
            isStop = True
            break
        for i in range(4):
            nr, nc = NR[i] + cur_r, NC[i] + cur_c
            if nr < 0 or nr >= R or nc < 0 or nc >= C or visit[nr][nc]:
                continue
            q.append((nr, nc)) if LAKE[nr][nc] == '.' else next_q.append((nr, nc))
            visit[nr][nc] = True
    q = next_q
    if isStop:
        break

    # melt ice
    for _ in range(len(water_q)):
        r, c = water_q.popleft()
        LAKE[r][c] = '.'
        for i in range(4):
            nr, nc = NR[i] + r, NC[i] + c
            if nr < 0 or nr >= R or nc < 0 or nc >= C or melt_visit[nr][nc]:
                continue
            if LAKE[nr][nc] == 'X':
                water_q.append((nr, nc))
                melt_visit[nr][nc] = True

    day += 1

print(day)
