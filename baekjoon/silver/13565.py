import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
map = [list(map(int, input().strip())) for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

for n in range(N):
  if map[0][n] == 0:
    map[0][n] = 2
    q.append((0, n))

while q:
  x, y = q.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<= nx <M and 0<= ny <N and map[nx][ny] == 0:
      map[nx][ny] = 2
      q.append((nx, ny))

if 2 in (map[0] and map[M-1]):
  print('YES')
else:
  print('NO')