# https://www.acmicpc.net/problem/1260
import sys, collections
def dfs(n):
    global dfs_seq
    for i in sorted(EDGES[n]):
        if not visited[i]:
            visited[i] = True
            dfs_seq.append(str(i))
            dfs(i)
def bfs(n):
    global bfs_seq
    q = collections.deque()
    q.append(n)
    visited = [False] * (N + 1)
    visited[n] = True
    while q:
        edge = q.popleft()
        for i in sorted(EDGES[edge]):
            if not visited[i]:
                visited[i] = True
                bfs_seq.append(str(i))
                q.append(i)

N, M, V = map(int, sys.stdin.readline().split())
EDGES = collections.defaultdict(list)
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    EDGES[n1].append(n2)
    EDGES[n2].append(n1)

dfs_seq, bfs_seq = [str(V)], [str(V)]
visited = [False] * (N + 1)
visited[V] = True
dfs(V)
bfs(V)
print(' '.join(dfs_seq))
print(' '.join(bfs_seq))
