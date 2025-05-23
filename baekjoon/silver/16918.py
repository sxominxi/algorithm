import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
map = [list(map(str, input().strip())) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_bomb_positions(m):
  bomb_position = []
  for r in range(R):
    for c in range(C):
      if m[r][c] == 'O':
        bomb_position.append([r, c])
  return bomb_position

def explode(m, bomb):
  new_map = [['O'] * C for _ in range(R)]
  for r, c in bomb:
    new_map[r][c] = '.'
    for i in range(4):
      nr = r + dx[i]
      nc = c + dy[i]
      if 0 <= nr < R and 0 <= nc < C:
        new_map[nr][nc] = '.'
  return new_map

if N == 1:
  for r in range(R):
    print(''.join(map[r]))
elif N % 2 == 0:
  for _ in range(R):
    print('O'* C)
else:
      # 시간 3초 상태 (1번 폭발)
    first_bombs = get_bomb_positions(map)
    first = explode(map, first_bombs)

    # 시간 5초 상태 (2번 폭발)
    second_bombs = get_bomb_positions(first)
    second = explode(first, second_bombs)

    # 홀수지만 N == 3이면 first, N == 5 이상이면 반복
    if N % 4 == 3:
        for row in first:
            print(''.join(row))
    else:
        for row in second:
            print(''.join(row))