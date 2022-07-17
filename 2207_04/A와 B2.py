# (12m) https://www.acmicpc.net/problem/12919
import sys
S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

is_change = 0
def dfs(cur_str):
    global is_change
    if len(cur_str) == len(S):
        if cur_str == S:
            is_change = 1
        return
    if cur_str[-1] == 'A':
        dfs(cur_str[:-1])
    if cur_str[0] == 'B':
        cur_str = cur_str[1:]
        dfs(cur_str[::-1])
dfs(T)
print(is_change)
