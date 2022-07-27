# (미해결)
# https://www.acmicpc.net/problem/17472
N, M = map(int, sys.stdin.readline().split())
BOARD = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
NR, NC = [0, 0, 1, -1], [1, -1, 0, 0]

def numbering(num, loc):
    q = collections.deque()
    q.append((loc[0], loc[1]))
    while q:
        r, c = q.popleft()
        BOARD[r][c] = num
        for i in range(4):
            nr, nc = r + NR[i], c + NC[i]
            if 0 <= nr < N and 0 <= nc < M and BOARD[nr][nc] == 1:
                q.append((nr, nc))

cnt = 0
for r in range(N):
    for c in range(M):
        if BOARD[r][c] == 1:
            numbering(cnt + 2, [r, c])
            cnt += 1

def find_bridge(start):
    distance = [1e9] * cnt
    distance[start - 2] = 0

    q = collections.deque()
    for r in range(N):
        for c in range(M):
            if BOARD[r][c] == start:
                for d in range(4):
                    q.append((r, c, d, 0))
    while q:
        cur_r, cur_c, d, bridge_length = q.popleft()
        nr, nc = cur_r + NR[d], cur_c + NC[d]
        if 0 <= nr < N and 0 <= nc < M:
            if BOARD[nr][nc] != 0 and BOARD[nr][nc] != start:
                distance[BOARD[nr][nc] - 2] = min(distance[BOARD[nr][nc] - 2], bridge_length)
                continue
            if BOARD[nr][nc] == 0:
                q.append((nr, nc, d, bridge_length + 1))
    return distance

bridges = []
for i in range(cnt):
    distance = find_bridge(i + 2)
    for j in range(i + 1, cnt):
        if 1 < distance[j] < 1e9:
            bridges.append((distance[j], i, j))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

bridges.sort()
result, parent = 0, [0] * 7
for i in range(1, cnt + 1):
    parent[i] = i

for d, start, end in bridges:
    if find_parent(parent, start) != find_parent(parent, end):
        union_parent(parent, start, end)
        result += d

print(result) if result != 0 else print(-1)
