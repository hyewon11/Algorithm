# https://www.acmicpc.net/problem/1700
import sys
N, K = map(int, sys.stdin.readline().split())
SEQUENCE = list(map(int, sys.stdin.readline().split()))

tab = []
cnt = 0
for i in range(K):
    num = SEQUENCE[i]
    if num in tab:
        continue
    if len(tab) < N:
        tab.append(num)
    else:
        cnt += 1
        not_in = list(set(tab) - set(SEQUENCE[i:]))
        if not_in:
            tab.remove(not_in[0])
        else:
            priority = []
            for num2 in SEQUENCE[i:]:
                if num2 in tab and num2 not in priority:
                    priority.append(num2)
            tab.remove(priority[-1])
        tab.append(num)
print(cnt)
