# (미해결) https://www.acmicpc.net/problem/20055
import sys, collections
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
robots = [False] * (2 * N + 1)

q = collections.deque()
q.append(0)
A[0] -= 1
level, up, down = 1, 0, N - 1
while A.count(0) < K:
    up = up - 1 if up != 0 else 2 * N - 1
    down = down - 1 if down != 0 else 2 * N - 1

    for _ in range(len(q)):
        loc = q.popleft()
        if loc == down:
            continue
        next_loc = loc + 1 if loc != 2 * N - 1 else 0
        if A[next_loc] > 0 and not robots[next_loc]:
            A[next_loc] -= 1
            q.append(next_loc)
        else:
            robots[next_loc] = True

    if A[up] > 0 and not robots[up]:
        q.append(up)
    level += 1
print(level)
