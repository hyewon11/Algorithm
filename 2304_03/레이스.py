# https://www.acmicpc.net/problem/1508
# binary search
import sys
N,M,K= map(int, sys.stdin.readline().split())
X = list(map(int, sys.stdin.readline().split()))

l, r, res = 1, X[-1] - X[0], ''
while l <= r:
    mid = (l + r) // 2
    cnt, cur, loc = 1, 0, '1'
    for i in range(1, K):
        if X[i] - X[cur] >= mid and cnt < M:
            cnt += 1
            cur = i
            loc += '1'
        else:
            loc += '0'

    if cnt < M:
        r = mid - 1
    else:
        l = mid + 1
        res = loc
print(res)
