# https://www.acmicpc.net/problem/17615
import sys
def dfs(is_red, is_right):
    global result
    cnt, char = 0, 'R' if is_red else 'B'
    if is_right:
        for i in range(N):
            if BALLS[i] == char:
                cnt += 1
            else:
                break
    else:
        for i in range(N - 1, -1, -1):
            if BALLS[i] == char:
                cnt += 1
            else:
                break
    result = min(result, red_cnt - cnt) if is_red else min(result, blue_cnt - cnt)

N = int(sys.stdin.readline())
BALLS = sys.stdin.readline().strip()

result = 1e9
red_cnt, blue_cnt = BALLS.count('R'), BALLS.count('B')

dfs(True, True)
dfs(True, False)
dfs(False, True)
dfs(False, False)
print(result)
