import sys
from collections import deque
input = sys.stdin.readline

N, M, T = map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
time = [0, 0]

for n in range(N):
  for m in range(M):
    if graph[n][m] == 2:
      gram = (n, m)
    elif graph[n][m] == 1:
      visited[n][m] = -1

# 칼 없이 
def nogram(map, visited, start):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  q = deque([start])
  # 방문처리 
  visited[start[0]][start[1]] = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위 설정 
      if 0<=nx<N and 0<=ny<M:
        # 아직 방문하지 않았고, 갈 수 있는 땅이라면 
        if visited[nx][ny] == 0 and map[nx][ny] != -1 :
          visited[nx][ny] = visited[x][y] + 1
          q.append((nx, ny))

  return visited[N-1][M-1] - visited[0][0]

# 칼 있이
def yesgram(visited, gram):
  x, y =gram
  if visited[x][y] > 0:
    togram = visited[x][y]
  else:
    return T + 1

  return togram + (N-y) + (M-x) - 3

time[0] = nogram(graph, visited, (0, 0))
time[1] = yesgram(visited, gram)

print(time)

if min(time) <= T and min(time) >= 0:
  print(min(time))
else:
  print('Fail')