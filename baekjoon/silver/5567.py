import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [-1]*(n+1)

q = deque([1])
visited[1] = 0

while q:
  x = q.popleft()
  for node in graph[x]:
    if visited[node] == -1:
      visited[node] = visited[x] + 1 
      q.append(node) 

# print(visited)
ans = 0
for v in visited:
  if 0 < v and v <= 2:
    ans += 1
print(ans)