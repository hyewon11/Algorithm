# https://www.acmicpc.net/problem/2422
import sys, itertools
N, M = map(int, sys.stdin.readline().split())
NOT_MIXED = [[False] * 201 for _ in range(201)]
for _ in range(M):
    num1, num2 = map(int, sys.stdin.readline().split())
    NOT_MIXED[num1][num2] = True
    NOT_MIXED[num2][num1] = True

cnt = 0
for sequence in itertools.combinations(range(1, N + 1), 3):
    is_stop = False
    for i in range(3):
        for j in range(i + 1, 3):
            if NOT_MIXED[sequence[i]][sequence[j]]:
                is_stop = True
    if not is_stop:
        cnt += 1
print(cnt)
