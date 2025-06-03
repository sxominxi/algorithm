import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
family = [[] for _ in range(n+1)]
visited = [-1]*(n+1)

for _ in range(m):
  x, y = map(int, input().split())
  family[x].append(y)
  family[y].append(x)

q = deque()
q.append(a)
visited[a] = 0

while q:
  node = q.popleft()
  for next in family[node]:
    if visited[next] == -1:
      visited[next] = visited[node] + 1
      q.append(next)

print(visited[b])