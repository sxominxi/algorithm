import sys
from collections import deque
input = sys.stdin.readline

def DFS(start):
  print(start, end=' ')
  global visited

  visited[start] = 1
  for node in range(1, N+1):
    if not visited[node] and graph[start][node]:
      DFS(node)

def BFS():
  global visited, q

  while q:
    x = q.popleft()
    print(x, end=' ')
    for node in range(1, N+1):
      if not visited[node] and graph[x][node]:
        visited[node] = 1
        q.append(node)

N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for m in range(M):
  a, b = map(int, input().split())
  graph[a][b] =1
  graph[b][a] = 1

q = deque()

visited = [0]*(N+1)
DFS(V)
print('')

visited = [0]*(N+1)
q.append(V)
visited[V] = 1
BFS()