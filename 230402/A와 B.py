# https://www.acmicpc.net/problem/12904
# Greedy

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

while T:
    if S == T:
        print(1)
        break
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]
else:
    print(0)
