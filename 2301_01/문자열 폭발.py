# https://www.acmicpc.net/problem/9935

import sys
WORDS = sys.stdin.readline().strip()
EXPLODED_WORDS = sys.stdin.readline().strip()
n = len(EXPLODED_WORDS)

stack = []
for ch in WORDS:
    stack.append(ch)
    if len(stack) >= n and ''.join(stack[-n:]) == EXPLODED_WORDS:
        for i in range(n):
            stack.pop()

print(''.join(stack)) if stack else print("FRULA")
