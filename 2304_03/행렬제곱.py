# https://www.acmicpc.net/problem/10830
# 분할정복

import sys
N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def mul_mat(m1, m2):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for t in range(N):
                result[i][j] += m1[i][t] * m2[t][j]
            result[i][j] %= 1000
    return result

def dfs(m, cnt):
    if cnt == 1:
        return m
    result = dfs(m, cnt // 2)
    return mul_mat(result, result) if cnt % 2 == 0 else mul_mat(mul_mat(result, result), m)

A = [[A[r][c] % 1000 for c in range(N)] for r in range(N)]
R = dfs(A, B)

for i in range(N):
    print(' '.join(list(map(str, R[i]))))
