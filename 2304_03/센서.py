# https://www.acmicpc.net/problem/2212
# Greedy
import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
LOCS = sorted(list(map(int, sys.stdin.readline().split())))

if N <= K:
    print(0)
else:
    distances = [LOCS[i + 1] - LOCS[i] for i in range(N - 1)]
    distances.sort(reverse=True)
    print(sum(distances[(K - 1):]))
