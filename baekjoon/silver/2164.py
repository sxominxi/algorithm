import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque()

for n in range(1, N+1):
    que.append(n)

while len(que) >= 2:
    que.popleft()
    que.append(que.popleft())

print(*que)