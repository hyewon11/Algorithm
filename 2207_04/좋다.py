import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

cnt = 0
A.sort()
for idx in range(N):
    left, right = 0, N - 2
    B = A[:idx] + A[idx + 1:]
    while left < right:
        if B[left] + B[right] < A[idx]:
            left += 1
        elif B[left] + B[right] > A[idx]:
            right -= 1
        else:
            cnt += 1
            break
print(cnt)
