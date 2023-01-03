# https://www.acmicpc.net/problem/1202
import sys, heapq
N, K = map(int, sys.stdin.readline().split())
GEMS = []
for _ in range(N):
    heapq.heappush(GEMS, list(map(int, sys.stdin.readline().split())))
WEIGHTS = [int(sys.stdin.readline()) for _ in range(K)]

WEIGHTS.sort()
q = []
total = 0
for w in WEIGHTS:
    while GEMS and w >= GEMS[0][0]:
        heapq.heappush(q, -heapq.heappop(GEMS)[1])
    if q:
        total -= heapq.heappop(q)
    elif not GEMS:
        break
print(total)
