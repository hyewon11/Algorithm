# (46m) https://www.acmicpc.net/problem/14658
import sys
N, M, L, K = map(int, sys.stdin.readline().split())
LOCATIONS = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

result = 0
for i in range(K):
    for j in range(K):
        cnt = 0
        for x, y in LOCATIONS:
            if LOCATIONS[i][0] <= x <= LOCATIONS[i][0] + L and LOCATIONS[j][1] <= y <= LOCATIONS[j][1] + L:
                cnt += 1
        result = max(result, cnt)
print(K - result)
