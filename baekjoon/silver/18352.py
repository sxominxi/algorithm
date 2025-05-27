import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [list() for _ in range(N+1)]
visited = [-1]*(N+1)

for m in range(M):
  A, B = map(int, input().split())
  graph[A].append(B)

visited[X] = 0
q = deque([X])

ans = []
flag = False
while q:
  x = q.popleft()
  for node in graph[x]:
    if visited[node] == -1:
      visited[node] = visited[x] + 1
      if visited[node] == K:
        ans.append(node)
      elif visited[node] < K:
        q.append(node)

if ans:
  for a in sorted(ans):
    print(a)
else:
  print(-1)