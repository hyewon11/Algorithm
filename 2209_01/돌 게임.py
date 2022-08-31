# https://www.acmicpc.net/problem/9655
import sys
N = int(sys.stdin.readline())
def dfs(rocks, turn):
    if rocks == 1 or rocks == 3:
        print("SK") if turn else print("CY")
        return
    if rocks == 2 or rocks == 4:
        dfs(rocks - 1, not turn)
    else:
        dfs(rocks - 3, not turn)
dfs(N, True)
