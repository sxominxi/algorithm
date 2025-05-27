import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
for m in range(M):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

visited = [-1] * (N+1)

q = deque()
q.append(S)
visited[S] = 0

while q:
  x = q.popleft()
  
  if x == E:
    print(visited[x])
    break

  for node in [x-1, x+1] + graph[x]:
    if 1 <= node <= N and visited[node] == -1:
      visited[node] = visited[x] + 1
      q.append(node)