import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
pixel = [[] for _ in range(N)]
for _ in range(N):
  RGB = list(map(int, input().split()))

  for i in range(len(RGB)//3):
    avg = (RGB[3*i]+RGB[3*i+1]+RGB[3*i+2])//3
    pixel[_].append(avg)

T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

newpixel = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for n in range(N):
  for m in range(M):
    if pixel[n][m] >= T:
      newpixel[n][m] = 255
    else:
      newpixel[n][m] = 0

def bfs(x, y):
  q = deque()
  q.append((x,y))
  visited[x][y] = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if not visited[nx][ny] and newpixel[nx][ny] == 255:
          visited[nx][ny] = 1
          q.append((nx, ny))

cnt = 0
for n in range(N):
  for m in range(M):
    if newpixel[n][m] == 255 and visited[n][m] == 0:
      bfs(n ,m)
      cnt += 1

print(cnt)