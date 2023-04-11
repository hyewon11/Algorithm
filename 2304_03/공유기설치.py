# https://www.acmicpc.net/problem/2110
# binary search
import sys
N,C = map(int, sys.stdin.readline().split())
X = [int(sys.stdin.readline()) for _ in range(N)]

X.sort()
l,r,res=1, X[-1] - X[0], 0
while l <= r:
    mid = (l + r) // 2
    cnt, cur = 1, 0
    for i in range(N):
        if X[i] - X[cur] >= mid:
            cnt += 1
            cur = i
    if cnt < C:
        r = mid - 1
    else:
        l = mid + 1
        res = mid
print(res)
