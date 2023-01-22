# https://www.acmicpc.net/problem/14003
import sys, bisect
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp, arr = [A[0]] , [0] * N
arr[0] = 1
for i in range(1, N):
    if A[i] > dp[-1]:
        dp.append(A[i])
        arr[i] = len(dp)
    else:
        idx = bisect.bisect_left(dp, A[i])
        dp[idx], arr[i] = A[i], idx + 1

max_idx = arr.index(max(arr))
max_value = arr[max_idx]
result = []
for i in range(max_idx, -1, -1):
    if arr[i] == max_value:
        result.append(A[i])
        max_value -= 1
result.reverse()
        
print(len(dp))
print(' '.join(list(map(str, result))))
