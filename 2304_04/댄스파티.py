# https://www.acmicpc.net/problem/2831
# Greedy

import sys
N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))
W = list(map(int, sys.stdin.readline().split()))

mp = [M[i] for i in range(N) if M[i] > 0]
mn = [M[i] for i in range(N) if M[i] < 0]
wp = [W[i] for i in range(N) if W[i] > 0]
wn = [W[i] for i in range(N) if W[i] < 0]
mp.sort()
mn.sort()
wp.sort()
wn.sort()

cnt = 0
l,r=0,len(mp) -1
while l < len(wn) and r > -1:
    if mp[r] + wn[l] < 0:
        cnt += 1
        l += 1
        r -= 1
    else:
        r -= 1

l,r=0,len(wp) -1
while l < len(mn) and r > -1:
    if wp[r] + mn[l] < 0:
        cnt += 1
        l += 1
        r -= 1
    else:
        r -= 1
print(cnt)
