import sys

T = int(sys.stdin.readline())

for _ in range(T):
    flag = 'YES'
    stack = []
    gualho = list(map(str, sys.stdin.readline().strip()))

    for g in gualho:
        if g == '(':
            stack.append('(')
        elif g == ')' and len(stack) >= 1:
            stack.pop()
        else:
            flag = 'NO'
            break
    
    if len(stack) != 0:
        flag = 'NO'

    print(flag)