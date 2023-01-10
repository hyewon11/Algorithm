# https://www.acmicpc.net/problem/1655
import sys, heapq
N = int(sys.stdin.readline())
NUMBERS = [int(sys.stdin.readline()) for _ in range(N)]
left_q, right_q = [], []
for num in NUMBERS:
    heapq.heappush(left_q, -num) if len(left_q) == len(right_q) else heapq.heappush(right_q, num)
    if len(right_q) and -left_q[0] > right_q[0]:
        left_max, right_max = -heapq.heappop(left_q), heapq.heappop(right_q)
        heapq.heappush(left_q, -right_max)
        heapq.heappush(right_q, left_max)
    print(-left_q[0])
