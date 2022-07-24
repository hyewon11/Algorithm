# https://www.acmicpc.net/problem/2531
import sys, collections
N, D, K, C = map(int, sys.stdin.readline().split())
SEQUENCE = [int(sys.stdin.readline()) for _ in range(N)]

left, right, result = 0, K - 1, 0
plates = collections.defaultdict(int)
for i in range(left, right + 1):
    num = SEQUENCE[i]
    if plates[num] == 0:
        result += 1
    plates[num] += 1

if plates[C] == 0:
    result += 1
plates[C] += 1

cnt = result
for i in range(1, N + 1):
    right = (right + 1) % N
    if plates[SEQUENCE[right]] == 0:
        cnt += 1
    plates[SEQUENCE[right]] += 1

    plates[SEQUENCE[left]] -= 1
    if plates[SEQUENCE[left]] == 0:
        cnt -= 1
    left = (left + 1) % N
    result = max(result, cnt)
print(result)
