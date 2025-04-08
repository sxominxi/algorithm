import sys

N = int(sys.stdin.readline())

stack = []
max_size = N

for n in range(N):
    order = list(map(int, sys.stdin.readline().split()))
    if order[0] == 1:
        stack.append(order[1])
    elif order[0] == 2:
        if len(stack) >= 1:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == 3:
        print(len(stack))
    elif order[0] == 4:
        if len(stack) >= 1:
            print(0)
        else:
            print(1)
    else:
        if len(stack) >= 1:
            print(stack[len(stack)-1])
        else:
            print(-1)