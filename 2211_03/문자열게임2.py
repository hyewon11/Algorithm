# https://www.acmicpc.net/problem/20437
import sys, re
T = int(sys.stdin.readline())
for _ in range(T):
    W = sys.stdin.readline()
    K = int(sys.stdin.readline())

    min_n, max_n = 1e9, -1
    for alphabet in set(W):
        if K == 1:
            min_n, max_n = 1, 1
            break
        indices = [i.start() for i in re.finditer(alphabet, W)]
        if len(indices) == K:
            n = indices[-1] - indices[0] + 1
            min_n = min(min_n, n)
            max_n = max(max_n, n)
        elif len(indices) > K:
            for i in range(len(indices) - K + 1):
                n = indices[i + K - 1] - indices[i] + 1
                min_n = min(min_n, n)
                max_n = max(max_n, n)

    if min_n != 1e9 and max_n != -1:
        print(min_n, max_n)
    else:
        print(-1)
