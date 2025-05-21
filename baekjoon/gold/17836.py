import sys
from collections import deque
input = sys.stdin.readline

N, M, T = map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(N)]
time = [0, 0]

# 그람 좌표 
gram = None
for n in range(N):
  for m in range(M):
    if graph[n][m] == 2:
      gram = (n, m)

# 하 상 좌 우 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 칼 없이 
def bfs(map, start):
  visited = [[-1]*M for _ in range(N)]
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
        if visited[nx][ny] == -1 :
          if map[nx][ny] != 1 :
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

  return visited

# 검 없이 BFS
nogram_time = bfs(graph, (0,0))[N-1][M-1]

# 검이 있을 경우, 검까지 거리 + 검에서 공주까지 직진 거리
yesgram_time = T+1
if gram:
  visited = bfs(graph, (0,0))
  togram = visited[gram[0]][gram[1]]
  if togram != -1:
    from_gram = (N - 1 - gram[0]) + (M - 1 - gram[1])
    yesgram_time = togram + from_gram
    # print(togram, from_gram)

# if nogram_time != -1 and nogram_time < yesgram_time:
#   min_time = nogram_time
# elif nogram_time != -1 and yesgram_time < nogram_time:
#   min_time = yesgram_time
# else:
#   min_time = T+1

if nogram_time == -1:
  nogram_time = T+1

min_time = min(nogram_time, yesgram_time)

# print(nogram_time)
# print(yesgram_time)
# print(min_time)
if min_time <= T:
    print(min_time)
else:
    print("Fail")