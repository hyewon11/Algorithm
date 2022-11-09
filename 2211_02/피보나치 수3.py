# https://www.acmicpc.net/problem/2749
# period = MOD//10 * 15
import sys
N = int(sys.stdin.readline().strip())

period = (10 ** 5)*15
fib = [0] * (period + 1)
fib[0], fib[1] = 0, 1
for i in range(2, period):
    fib[i] = (fib[i - 2] + fib[i - 1])%1000000

print(fib[N%period])
