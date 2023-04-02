# https://www.acmicpc.net/problem/18185
# Greedy
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split())) + [0, 0]

result = 0
for i in range(N):
    if A[i + 1] > A[i + 2]:
        # 2개 우선
        cnt = min(A[i], A[i + 1] - A[i + 2])
        result += 5 * cnt
        A[i], A[i + 1] = A[i] - cnt, A[i + 1] - cnt

        cnt = min(A[i], A[i + 2])
        result += 7 * cnt
        A[i], A[i + 1], A[i + 2] = A[i] - cnt, A[i + 1] - cnt, A[i + 2] - cnt

    else:
        # 3개 우선
        cnt = min(A[i], A[i + 1], A[i + 2])
        result += 7 * cnt
        A[i], A[i + 1], A[i + 2] = A[i] - cnt, A[i + 1] - cnt, A[i + 2] - cnt

        cnt = min(A[i], A[i + 1])
        result += 5 * cnt
        A[i], A[i + 1] = A[i] - cnt, A[i + 1] - cnt

    result += A[i] * 3
    A[i] = 0
print(result)
