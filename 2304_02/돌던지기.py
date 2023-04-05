# https://www.acmicpc.net/problem/3025
# 구현

R, C = map(int, sys.stdin.readline().split())
MAP = [list(sys.stdin.readline().strip()) for _ in range(R)]
N = int(sys.stdin.readline())
COLS = [int(sys.stdin.readline()) - 1 for _ in range(N)]

paths = collections.defaultdict(list)
for c in COLS:
    while paths[c]:
        cur_r, cur_c = paths[c][-1]
        if MAP[cur_r][cur_c] == '.':
            break
        paths[c].pop()
    if paths[c]:
        cur_r, cur_c = paths[c].pop()
    else:
        cur_r, cur_c = 0, c

    while cur_r < R - 1:
        paths[c].append((cur_r, cur_c))
        if MAP[cur_r + 1][cur_c] == '.':
            cur_r += 1
            continue
        if MAP[cur_r + 1][cur_c] == 'X':
            break
        if 0 <= cur_c - 1 and MAP[cur_r][cur_c - 1] == '.' and MAP[cur_r + 1][cur_c - 1] == '.':
            cur_r, cur_c = cur_r + 1, cur_c - 1
            continue
        if cur_c + 1 < C and MAP[cur_r][cur_c + 1] == '.' and MAP[cur_r + 1][cur_c + 1] == '.':
            cur_r, cur_c = cur_r + 1, cur_c + 1
            continue
        break
    MAP[cur_r][cur_c] = 'O'

for r in range(R):
    print(''.join(MAP[r]))
