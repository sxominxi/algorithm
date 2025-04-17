import sys
from collections import deque

TC = int(sys.stdin.readline())

for _ in range(TC):
    N, M = map(int, sys.stdin.readline().split())
    importance = deque(list(map(int, sys.stdin.readline().split())))

    ans = 0
    while importance:
        maxnum = max(importance)
        front = importance.popleft()
        M -= 1

        if maxnum == front:
            ans += 1
            if M < 0:
                print(ans)
                break
        else:
            importance.append(front)
            if M < 0:
                M = len(importance) - 1