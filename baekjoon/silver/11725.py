# 트리의 부모 찾기
import sys
from collections import deque
input = sys.stdin.readline

def BFS(x):
  queue = deque([x]) # 탐색할 노드
  visited[x] = 1

  while queue:
    node = queue.popleft()
    for g in graph[node]:
      if not visited[g]:
        visited[g] = 1
        parent[g] = node 
        queue.append(g)

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [1]*(N+1)
visited = [0]*(N+1)

for _ in range(N-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

BFS(1)

for i in range(2, N + 1):
  print(parent[i])