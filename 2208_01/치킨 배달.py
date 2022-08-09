# 
import sys, itertools
N, M = map(int, sys.stdin.readline().split())
CITY = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

chickens = [(r, c) for r in range(N) for c in range(N) if CITY[r][c] == 2]
houses = [(r, c) for r in range(N) for c in range(N) if CITY[r][c] == 1]
result = 1e9

for sequence in itertools.combinations(range(len(chickens)), M):
    distance = 0
    for house_idx in range(len(houses)):
        h_r, h_c = houses[house_idx]
        min_distance = 1e9
        for chicken_idx in sequence:
            c_r, c_c = chickens[chicken_idx]
            min_distance = min(min_distance, abs(h_r - c_r) + abs(h_c - c_c))
        distance += min_distance
    result = min(result, distance)

print(result)
