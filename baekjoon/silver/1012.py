import sys 
from collections import deque
input = sys.stdin.readline

def bfs(x, y, cnt):
  q = deque()
  q.append((x,y))

  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<N and 0<=ny<M and farm[nx][ny] == 1:
        farm[nx][ny] = cnt
        q.append((nx, ny))

T = int(input())
for t in range(T):
  M, N, K = map(int, input().split())
  farm = [[0]*M for _ in range(N)]

  for k in range(K):
    X, Y = map(int, input().split())
    farm[Y][X] = 1
  
  cnt = 1
  for n in range(N):
    for m in range(M):

      if farm[n][m] == 1:
        cnt += 1
        bfs(n, m, cnt)

  print(cnt-1)