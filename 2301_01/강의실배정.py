# https://www.acmicpc.net/problem/11000
import sys, heapq
N = int(sys.stdin.readline())
CLASSES = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
CLASSES.sort()

q = [CLASSES[0][1]]
for i in range(1, N):
    if CLASSES[i][0] < q[0]:
        heapq.heappush(q, CLASSES[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, CLASSES[i][1])

print(len(q))
