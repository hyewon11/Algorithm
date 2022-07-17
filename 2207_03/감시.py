# https://www.acmicpc.net/problem/15683 (삼성)
import sys, copy
def monitor(r, c, direction, n, new_map):
    # 상하좌우
    if direction == 0:
        for nr in range(r - 1, -1, -1):
            if new_map[nr][c] == 0:
                new_map[nr][c] = 7
            if new_map[nr][c] == 6:
                break
    elif direction == 1:
        for nr in range(r + 1, N):
            if new_map[nr][c] == 0:
                new_map[nr][c] = 7
            if new_map[nr][c] == 6:
                break
    elif direction == 2:
        for nc in range(c - 1, -1, -1):
            if new_map[r][nc] == 0:
                new_map[r][nc] = 7
            if new_map[r][nc] == 6:
                break
    elif direction == 3:
        for nc in range(c + 1, M):
            if new_map[r][nc] == 0:
                new_map[r][nc] = 7
            if new_map[r][nc] == 6:
                break
    return new_map

N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cctvs, cctv_5 = [], []
for r in range(N):
    for c in range(M):
        if 1 <= MAP[r][c] <= 4:
            cctvs.append((MAP[r][c], r, c))
        if MAP[r][c] == 5:
            cctv_5.append((r, c))

for r, c in cctv_5:
    for i in range(4):
        MAP = monitor(r, c, i, 0, MAP)

result = 1e9
def dfs(idx, cur_map):
    global result
    if idx == len(cctvs):
        cnt = 0
        for r in range(N):
            for c in range(M):
                if cur_map[r][c] == 0:
                    cnt += 1
        result = min(result, cnt)
        return

    cctv_num, r, c = cctvs[idx]
    if cctv_num == 1:
        for d in range(4):
            new_map = monitor(r, c, d, 0, copy.deepcopy(cur_map))
            dfs(idx + 1, new_map)
    elif cctv_num == 2:
        for d in range(2):
            new_map = monitor(r, c, 2 * d, 0, copy.deepcopy(cur_map))
            new_map = monitor(r, c, 2 * d + 1, 0, new_map)
            dfs(idx + 1, new_map)
    elif cctv_num == 3:
        for d1, d2 in [(0, 3), (0, 2), (1, 3), (1, 2)]:
            new_map = monitor(r, c, d1, 0, copy.deepcopy(cur_map))
            new_map = monitor(r, c, d2, 0, new_map)
            dfs(idx + 1, new_map)
    elif cctv_num == 4:
        for d1, d2, d3 in [(0, 1, 2), (0, 2, 3), (1, 2, 3), (0, 1, 3)]:
            new_map = monitor(r, c, d1, 0, copy.deepcopy(cur_map))
            new_map = monitor(r, c, d2, 0, new_map)
            new_map = monitor(r, c, d3, 0, new_map)
            dfs(idx + 1, new_map)
dfs(0, MAP)
print(result)
