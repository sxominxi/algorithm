import sys
input = sys.stdin.readline

R, C = map(int, input().split())
map = [list(map(str, input().strip())) for _ in range(R)]
land = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

trans = []
for r in range(R):
  for c in range(C):
    if map[r][c] == 'X':
      land.append([r, c])

      sea = 0
      for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]   
        if 0<=nx<R and 0<=ny<C:
          if map[nx][ny] == '.':
            sea += 1
        else:
          sea+= 1
        
        if sea >= 3:
          trans.append([r, c])

if len(trans) > 0:
  for i in range(len(trans)):
    map[trans[i][0]][trans[i][1]] = '.'

x_min, y_min = R, C
x_max, y_max = -1, -1
for r in range(R):
    for c in range(C):
        if map[r][c] == 'X':
            x_min = min(x_min, r)
            y_min = min(y_min, c)
            x_max = max(x_max, r)
            y_max = max(y_max, c)

for x in range(x_min, x_max+1):
  print(''.join(map[x][y_min:y_max+1]))