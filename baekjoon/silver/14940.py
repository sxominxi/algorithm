import sys
from collections import deque
input = sys.stdin.readline

def bfs(map, visited, start):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  q = deque([start])
  # 방문처리 
  visited[start[0]][start[1]] = 0

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위 설정 
      if 0<=nx<N and 0<=ny<M:
        # 아직 방문하지 않았고, 갈 수 있는 땅이라면 
        if visited[nx][ny] == -1 and map[nx][ny] == 1:
          visited[nx][ny] = visited[x][y] + 1
          q.append((nx, ny))

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

for i in range(N):
  for j in range(M):
    # 출발 지점
    if map[i][j] == 2:
      start = (i, j)
    # 못가는 지점 
    elif map[i][j] == 0:
      # 0으로 출력하래 
      visited[i][j] = 0

bfs(map, visited, start)

for i in range(N):
    for j in range(M):
        print(visited[i][j], end=' ')
    print('')
