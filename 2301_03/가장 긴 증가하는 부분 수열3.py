# https://www.acmicpc.net/problem/12738
import sys, bisect
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [A[0]]
for i in range(1, N):
    if A[i] > dp[-1]:
        dp.append(A[i])
    else:
        idx = bisect.bisect_left(dp, A[i])
        dp[idx] = A[i]

print(len(dp))
