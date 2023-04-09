# https://www.acmicpc.net/problem/2036
# Greedy

import sys
N = int(sys.stdin.readline())
M_NUMS, P_NUMS = [], []
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    P_NUMS.append(num) if num > 0 else M_NUMS.append(num)

M_NUMS.sort()
P_NUMS.sort(reverse=True)
i, result = 0, 0

while i < len(P_NUMS):
    if i == len(P_NUMS) - 1:
        result += P_NUMS[i]
        break
    if P_NUMS[i] == 1 or P_NUMS[i + 1] == 1:
        result += P_NUMS[i] + P_NUMS[i + 1]
    else:
        result += P_NUMS[i] * P_NUMS[i + 1]
    i += 2

i = 0
while i < len(M_NUMS):
    if i == len(M_NUMS) - 1:
        result += M_NUMS[i]
        break
    result += M_NUMS[i] * M_NUMS[i + 1]
    i += 2

print(result)
