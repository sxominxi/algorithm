import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0 , 0, -1, 1]


def bfs(x, y):
  global visited
  q = deque()
  q.append((x, y))
  visited[x][y] = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if miro[nx][ny] == 1 and visited[nx][ny] == 0:
          q.append((nx, ny))
          visited[nx][ny] += visited[x][y] + 1

bfs(0, 0)
print(visited[N-1][M-1])