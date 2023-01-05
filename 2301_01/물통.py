# https://www.acmicpc.net/problem/14867
import sys, collections
A, B, C, D = map(int, sys.stdin.readline().split())

q = collections.deque()
q.append((0, 0, 0))
visit = collections.defaultdict(int)
visit[(0, 0)] = True
result = 1e9
while q:
    cur_a, cur_b, cnt = q.popleft()

    if cur_a == C and cur_b == D:
        result = min(result, cnt)
        break

    for next_a, next_b in [(A, cur_b), (cur_a, B), (0, cur_b), (cur_a, 0)]:
        if not visit[(next_a, next_b)]:
            visit[(next_a, next_b)] = True
            q.append((next_a, next_b, cnt + 1))
    # Move
    if cur_a <= B - cur_b:
        if not visit[(0, cur_b + cur_a)]:
            visit[(0, cur_b + cur_a)] = True
            q.append((0, cur_b + cur_a, cnt + 1))
    else:
        if not visit[(cur_a - B + cur_b, B)]:
            visit[(cur_a - B + cur_b, B)] = True
            q.append((cur_a - B + cur_b, B, cnt + 1))

    if cur_b <= A - cur_a:
        if not visit[(cur_b + cur_a, 0)]:
            visit[(cur_b + cur_a, 0)] = True
            q.append((cur_b + cur_a, 0, cnt + 1))
    else:
        if not visit[(A, cur_b - A + cur_a)]:
            visit[(A, cur_b - A + cur_a)] = True
            q.append((A, cur_b - A + cur_a, cnt + 1))

print(result) if result != 1e9 else print(-1)
