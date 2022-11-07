# https://www.acmicpc.net/problem/25757

import sys, collections
first_input = sys.stdin.readline().split()
N, GAMETYPE = int(first_input[0]), first_input[1]
PLAYERS = collections.defaultdict(int)

for _ in range(N):
    PLAYERS[sys.stdin.readline()] = 1

N = len(PLAYERS.items())
if GAMETYPE == "Y":
    print(N)
elif GAMETYPE == "F":
    print(N // 2)
else:
    print(N // 3)
