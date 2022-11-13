# https://www.acmicpc.net/problem/11401
# factorial 함수 재귀로 하면 시간 초과 발생
import sys
def factorial(n):
    res = 1
    for i in range(2, n+1):
        res = res * i % mod
    return res

def cal(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    tmp = cal(n, k//2)
    return tmp * tmp * n % mod if k % 2 else tmp * tmp % mod

N, K = map(int, sys.stdin.readline().split())
mod = 1000000007
res = factorial(N) * cal(factorial(N - K) * factorial(K) % mod, mod - 2)
print(res % mod)
