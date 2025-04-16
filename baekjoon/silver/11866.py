import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

josephu = deque([i for i in range(1, N+1)])
ans = []

while len(josephu) != 0:
    for _ in range(K-1):
        josephu.append(josephu.popleft())

    ans.append(str(josephu.popleft()))

print('<' + ', '.join(ans) + '>')