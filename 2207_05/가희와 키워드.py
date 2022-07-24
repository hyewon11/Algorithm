# https://www.acmicpc.net/problem/22233
import sys, collections
N, M = map(int, sys.stdin.readline().split())
MEMO_KEYWORDS = collections.defaultdict(int)
for _ in range(N):
    MEMO_KEYWORDS[sys.stdin.readline().strip()] = 1
BLOG_KEYWORDS = [sys.stdin.readline().strip().split(',') for _ in range(M)]

cnt = N
for writing in BLOG_KEYWORDS:
    for keyword in writing:
        if MEMO_KEYWORDS[keyword] > 0:
            cnt -= 1
            MEMO_KEYWORDS[keyword] = -1
    print(cnt)
