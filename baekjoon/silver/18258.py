import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque()

for n in range(N):
    input = list(map(str, sys.stdin.readline().split()))

    if input[0] == 'push':
        que.append(input[1])
    elif input[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif input[0] == 'size':
        print(len(que))
    elif input[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif input[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif input[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)