# https://www.acmicpc.net/problem/2740
# 구현
import sys
N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M, K = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

result = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for t in range(M):
            result[i][j] += A[i][t] * B[t][j]

for i in range(N):
    print(' '.join(list(map(str, result[i]))))
