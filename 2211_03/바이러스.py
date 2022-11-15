# https://www.acmicpc.net/problem/2606
import sys, collections
N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
PAIRS = collections.defaultdict(list)
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    PAIRS[n1].append(n2)
    PAIRS[n2].append(n1)

cnt = 0
q = collections.deque()
q.append(1)
visited = [False] * (N + 1)
visited[1] = True
while q:
    n = q.popleft()
    for i in PAIRS[n]:
        if not visited[i]:
            cnt += 1
            visited[i] = True
            q.append(i)
print(cnt)
