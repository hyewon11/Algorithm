# https://www.acmicpc.net/problem/9019
import sys, collections
T = int(sys.stdin.readline())
LIST = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
for i in range(T):
    A, B = LIST[i]

    visit = collections.defaultdict(int)
    q = collections.deque()
    q.append((A, ''))
    while q:
        num, cal_seq = q.popleft()
        if num == B:
            print(cal_seq)
            break

        str_num = str(num).zfill(4)
        d1, d2, d3, d4 = str_num[0], str_num[1],str_num[2],str_num[3]
        for next_num, direction in [(num * 2 % 10000, 'D'), (int(d2 + d3 + d4 + d1), 'L'), (int(d4 + d1 + d2 + d3), 'R')]:
            if not visit[next_num]:
                visit[next_num] = True
                q.append((next_num, cal_seq + direction))           
        # S
        if num == 0:
            if not visit[9999]:
                visit[9999] = True
                q.append((9999, cal_seq + 'S'))
        else:
            if not visit[num - 1]:
                visit[num - 1] = True
                q.append((num - 1, cal_seq + 'S'))
