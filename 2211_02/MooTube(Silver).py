# https://www.acmicpc.net/problem/15591 - bfs
import sys, collections
N, Q = map(int, sys.stdin.readline().split())

USADO = collections.defaultdict(list)
for _ in range(N - 1):
    p, q, r = map(int, sys.stdin.readline().split())
    USADO[p].append((q, r))
    USADO[q].append((p, r))

for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    q = collections.deque()
    visit, min_value = [False] * (N + 1), 0

    visit[v] = True
    for u_q, u_r in USADO[v]:
        q.append((u_q, u_r))
        visit[u_q] = True

    while q:
        node, u = q.popleft()
        if u >= k:
            min_value += 1
            for u_q, u_r in USADO[node]:
                if not visit[u_q]:
                    q.append((u_q, min(u, u_r)))
                    visit[u_q] = True

    print(min_value)
