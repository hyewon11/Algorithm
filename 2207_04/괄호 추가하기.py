# (1h) https://www.acmicpc.net/problem/16637
import sys
def calculate(num1, num2, op):
    num1, num2 = int(num1), int(num2)
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    else:
        return num1 * num2

def exp_calculate(idx, exp, num, cnt):
    global result
    if idx > N // 2 - cnt:
        result = max(num, result)
        return
    exp_calculate(idx + 1, exp, calculate(num, exp[2 * idx], exp[2 * idx - 1]), cnt)

def dfs(idx, exp, cnt):
    if idx >= N - 1 + cnt * 2:
        new_exp = []
        flag = False
        for i in range(len(exp)):
            if exp[i] == ')':
                flag = False
                continue
            elif exp[i] == '(':
                flag = True
                new_exp.append(str(calculate(exp[i + 1], exp[i + 3], exp[i + 2])))
            else:
                if flag:
                    continue
                new_exp.append(exp[i])
        exp_calculate(1, new_exp, int(new_exp[0]), cnt)
        return
    dfs(idx + 2, exp, cnt)
    dfs(idx + 6, exp[:idx] + '(' + exp[idx: idx + 3] + ')' + exp[idx + 3:], cnt + 1)

N = int(sys.stdin.readline())
EXPRESSION = sys.stdin.readline().strip()
result = -1e9

if N <= 2:
    print(EXPRESSION)
elif N == 3:
    print(calculate(EXPRESSION[0], EXPRESSION[2], EXPRESSION[1]))
else:
    dfs(0, EXPRESSION, 0)
    print(result)
