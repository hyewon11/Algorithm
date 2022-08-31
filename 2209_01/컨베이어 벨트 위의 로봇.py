# https://www.acmicpc.net/problem/20055

import sys, collections
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
visit = [False] * (2 * N)
q = collections.deque()

stage, up, down = 1, 0, N - 1
while True:
    # rotate Conveyor belt
    up, down = up - 1, down - 1
    if up == -1:
        up = 2 * N - 1
    if down == -1:
        down = 2 * N - 1
    
    # move robots
    for _ in range(len(q)):
        loc = q.popleft()
        if loc == down:
            visit[loc] = False
            continue
        else:
            next_loc = (loc + 1) % (2 * N)
            if visit[next_loc] or A[next_loc] == 0:
                q.append(loc)
            else:
                visit[loc] = False
                A[next_loc] -= 1
                if next_loc != down:
                    q.append(next_loc)
                    visit[next_loc] = True
    
    # put the robot on the belt
    if not visit[up] and A[up] > 0:
        A[up] -= 1
        visit[up] = True
        q.append(up)
    
    # check stop
    cnt = 0
    for i in range(2 * N):
        if A[i] <= 0:
            cnt += 1
    if cnt >= K:
        break
    stage += 1

print(stage)
