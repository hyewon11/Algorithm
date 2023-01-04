# https://www.acmicpc.net/problem/1039
import sys
N, K = map(int, sys.stdin.readline().split())
N = str(N)
n_length = len(N)

result = -1
visit = [[False] * 11 for _ in range(1000001)]
def dfs(k, num):
    global result
    if k <= 0:
        result = max(result, int(''.join(num)))
        return

    for i in range(n_length):
        for j in range(i + 1, n_length):
            tmp = ''.join(num)
            copy_num = tmp[:i] + tmp[j] + tmp[i+1:j] + tmp[i] + tmp[j + 1:]
            if copy_num[0] != '0' and not visit[int(copy_num)][k - 1]:
                visit[int(copy_num)][k - 1] = True
                dfs(k - 1, list(copy_num))
visit[int(N)][K] = True
dfs(K, list(N))
print(result)
