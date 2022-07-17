# https://www.acmicpc.net/problem/1238
import sys, heapq
def dijkstra(start, end):
    distance, q = [1e9] * (N + 1), []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        t, cur = heapq.heappop(q)
        if distance[cur] < t:
            continue
        for node in ROAD_TIME[cur]:
            cost = t + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))
    return distance

N, M, X = map(int, sys.stdin.readline().split())
ROAD_TIME = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, t = map(int, sys.stdin.readline().split())
    ROAD_TIME[start].append([end, t])

result = 0
d = [[0] * N for _ in range(2)]
for i in range(N):
    if i + 1 == X:
        d[1] = dijkstra(X, X)[1:]
        d[0][X - 1] = d[1][X - 1]
    else:
        d[0][i] = dijkstra(i + 1, X)[X]

for i in range(N):
    result = max(result, d[0][i] + d[1][i])
print(result)
