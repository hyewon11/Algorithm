# https://www.acmicpc.net/problem/13913
import sys, collections
N, K = map(int, sys.stdin.readline().split())

q = collections.deque()
q.append((N, str(N), 1))
visit = collections.defaultdict(int)
visit[N] = 1
while q:
    cur, locations, cnt = q.popleft()
    if cur == K:
        print(cnt - 1)
        print(locations)
        break

    for num in (cur + 1, cur - 1, cur * 2):
        if 0 <= num <= 100000 and visit[num] == 0:
            visit[num] = 1
            q.append((num, locations + ' ' + str(num), cnt + 1))
