# https://www.acmicpc.net/problem/19644
# Greedy

import sys
L = int(sys.stdin.readline())
Ml, Mk  = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())
Z = [int(sys.stdin.readline()) for _ in range(L)]

arr = [0] * 3000001
for i in range(1, L + 1):
    d = arr[i - 1] - arr[(i - 1) // Ml] + Mk
    if Z[i - 1] <= arr[i - 1] - arr[(i-1) // Ml] + Mk:
        arr[i] = arr[i - 1] + Mk
    else:
        if C:
            C -= 1
            arr[i] = arr[i - 1]
        else:
            print("NO")
            break
else:
    print("YES")
