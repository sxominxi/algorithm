import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
Ai = [0]
Ai.extend(list(map(int, input().split())))
s = int(input())

visited = [-1]*(n+1)

q = deque()
q.append(s)

while q:
  node = q.popleft()
  visited[node] += 1

  next = Ai[node]
  if (node - next) >= 1:
    q.append(node-next)
  if (node + next) <= n:
    q.append(node + next)

ans = 0
for v in visited:
  if v >-1:
    ans += 1
print(ans)