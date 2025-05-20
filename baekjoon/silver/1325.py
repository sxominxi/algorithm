import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
trust = [[] for _ in range(N+1)]

for _ in range(M):
  A,B = map(int, input().split())
  trust[B].append(A)

def bfs(start):
  visited = [0]*(N+1)
  q = deque([start])
  visited[start] = 1
  cnt =1

  while q:
    node = q.popleft()
    for next in trust[node]:
      if not visited[next]:
        visited[next]= 1
        q.append(next)
        cnt += 1
  
  return cnt

max_count = 0
result = []
for i in range(1, N + 1):
    cnt = bfs(i)
    if cnt > max_count:
        max_count = cnt
        result = [i]
    elif cnt == max_count:
        result.append(i)

print(*result)