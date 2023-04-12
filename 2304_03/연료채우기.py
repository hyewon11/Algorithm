# https://www.acmicpc.net/problem/1826
# Greedy 
import sys, heapq
N = int(sys.stdin.readline())
STATIONS = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
L, P = map(int, sys.stdin.readline().split())

STATIONS.append([L, 0])
STATIONS.sort(key=lambda x: x[0])
gases = []
cnt, cur_gas = 0, P
for i in range(N + 1):
    if cur_gas - STATIONS[i][0] < 0:
        while gases:
            cur_gas -= heapq.heappop(gases)
            cnt += 1
            if cur_gas - STATIONS[i][0] >= 0:
                break
    if len(gases) == 0 and cur_gas - STATIONS[i][0] < 0:
        cnt = -1
        break
    else:
        heapq.heappush(gases, -STATIONS[i][1])
print(cnt)
