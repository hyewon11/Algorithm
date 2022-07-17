# https://www.acmicpc.net/problem/13549
import sys, collections
N, K = map(int, sys.stdin.readline().split())
dp = [1e9] * 100001

q = collections.deque()
q.append(N)
dp[N] = 0
while q:
    cur_loc = q.popleft()
    if cur_loc == K:
        print(dp[K])
        break
    for i in [-1, 1]:
        if 0 <= cur_loc + i <= 100000 and dp[cur_loc] + 1 <= dp[cur_loc + i]:
            q.append(cur_loc + i)
            dp[cur_loc + i] = dp[cur_loc] + 1
    if cur_loc * 2 <= 100000 and dp[cur_loc] <= dp[cur_loc * 2]:
        q.append(cur_loc * 2)
        dp[cur_loc * 2] = dp[cur_loc]
