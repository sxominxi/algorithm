import sys
from collections import deque
input = sys.stdin.readline

N= int(input())
info = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1 ,1, 0, 0]
dy = [0, 0, -1, 1]

danji = 2
def find(x, y):
  global info, danji
  cnt = 1
  q = deque()
  q.append((x, y))
  info[x][y] = danji

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<N and 0<=ny<N:
        if info[nx][ny] == 1:
          q.append((nx, ny))
          info[nx][ny] = danji
          cnt += 1

  danji += 1
  return cnt

ans = []
for i in range(N):
  for j in range(N):
    if info[i][j]==1:
      cnt = find(i,j)
      ans.append(cnt)

print(len(ans))  # 단지 수
for x in sorted(ans):
  print(x)