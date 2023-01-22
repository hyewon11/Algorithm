# https://www.acmicpc.net/problem/14002
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_idx = dp.index(max(dp))
max_value = dp[max_idx]
arr = []
for i in range(max_idx, -1, -1):
    if dp[i] == max_value:
        arr.append(A[i])
        max_value -= 1
arr.reverse()

print(max(dp))
print(' '.join(list(map(str, arr))))
