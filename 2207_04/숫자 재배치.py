# (5m) https://www.acmicpc.net/problem/16943
import sys, itertools
A, B = sys.stdin.readline().strip().split()
B = int(B)
C = -1
for sequence in itertools.permutations(A):
    if sequence[0] == '0':
        continue
    num = int(''.join(sequence))
    if num < B:
        C = max(num, C)
print(C)
