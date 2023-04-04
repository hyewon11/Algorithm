# https://www.acmicpc.net/problem/1956
# Graph & Floyd-Warshall

import sys, copy
V, E = map(int, sys.stdin.readline().split())
ROADS = [[1e9] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    ROADS[a][b] = c

distances = copy.deepcopy(ROADS)
for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

result = 1e9
for i in range(1, V+1):
    for j in range(1, V+1):
        if distances[i][j] < 1e9 and distances[j][i] < 1e9:
            result = min(result, distances[i][j] + distances[j][i])

print(result) if result != 1e9 else print(-1)
