# https://www.acmicpc.net/problem/17088
import sys
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

result = 1e9
if N <= 2:
    result = 0

def dfs(idx, cnt):
    global result
    if idx > 2 and B[0] - B[1] != B[idx - 2] - B[idx - 1]:
        return

    if idx == N:
        result = min(result, cnt)
        return

    B[idx] -= 1
    dfs(idx + 1, cnt + 1)
    B[idx] += 1

    dfs(idx + 1, cnt)

    B[idx] += 1
    dfs(idx + 1, cnt + 1)
    B[idx] -= 1

dfs(0, 0)
print(result) if result != 1e9 else print(-1)
