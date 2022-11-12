# https://www.acmicpc.net/problem/10021
import sys, heapq
N, C = map(int, sys.stdin.readline().split())
POINT =[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
distance, p = [], [i for i in range(N + 1)]
for i in range(N):
    for j in range(i + 1, N):
        d = (POINT[i][0] - POINT[j][0]) ** 2 + (POINT[i][1] - POINT[j][1]) ** 2
        if d >= C:
            heapq.heappush(distance, (d, i + 1, j + 1))

def find(u):
    if p[u] == u:
        return u
    else:
        p[u] = find(p[u])
        return p[u]

def union(u, v):
    r1, r2 = find(u), find(v)
    if r1 == r2:
        return False
    else:
        p[r2] = r1
        return True

min_cost, cnt = 0, 0
while distance:
    d, u, v = heapq.heappop(distance)
    if union(u, v):
        min_cost += d
        cnt += 1
        if cnt == N - 1:
            break

print(min_cost) if cnt >= N - 1 else print(-1)
