# https://www.acmicpc.net/problem/1522
import sys
INPUTS = sys.stdin.readline().strip()
a_cnt = INPUTS.count('a')
res = 1e9
for i in range(len(INPUTS)):
    if i + a_cnt <= len(INPUTS):
        b_cnt = INPUTS[i:i + a_cnt].count('b')
    else:
        b_cnt = INPUTS[i:].count('b') + INPUTS[:a_cnt - len(INPUTS) + i].count('b')
    res = min(res, b_cnt)
print(res)
