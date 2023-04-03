# https://www.acmicpc.net/problem/1459
# Greedy
import sys
X, Y, W, S = map(int, sys.stdin.readline().split())

# 대각선 이동
cross_cnt, cross_time = min(X, Y), min(S, W * 2)
result = cross_cnt * cross_time

# 대각 + 대각 OR 선 이동
if X - cross_cnt >= 2 and cross_time * 2 < W * 2:
    cnt = (X - cross_cnt) // 2
    result += (cnt * cross_time * 2 + (X - cross_cnt - cnt*2) * W)
else:
    result += (X - cross_cnt) * W

if Y - cross_cnt >= 2 and cross_time * 2 < W * 2:
    cnt = (Y - cross_cnt) // 2
    result += (cnt * cross_time * 2 + (Y - cross_cnt - cnt*2) * W)
else:
    result += (Y - cross_cnt) * W

print(result)
