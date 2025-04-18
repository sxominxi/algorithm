import sys
from collections import deque

N = int(sys.stdin.readline())
board = [[0]*N for _ in range(N)]

# 사과 개수
K = int(sys.stdin.readline())
# 사과 위치 = -1
for k in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = -1

# 뱀의 머리
snake_p, snake_q = 0, 0
# 방향: 오른(0), 아래(1), 왼(2), 위(3)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0  # 시작은 오른쪽

# 방향 전환 정보 저장
L = int(sys.stdin.readline())
turns = dict()
for _ in range(L):
    sec, dir = sys.stdin.readline().split()
    turns[int(sec)] = dir

# 뱀의 몸길이 
snake = deque()
snake.append((0, 0))
# 뱀의 위치 = 1
board[0][0] = 1 

# 시간 -> 구하려는 것
time = 0

while True:
    time += 1
    nx = snake_p + dx[direction]
    ny = snake_q + dy[direction]

    # 뱀이 벽을 만나거나 자기 자신을 만나면 끝
    if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 1:
        break

    # 3. 머리 이동
    if board[nx][ny] == -1:  # 사과
        board[nx][ny] = 1
        snake.append((nx, ny))
    else:
        board[nx][ny] = 1
        snake.append((nx, ny))
        tx, ty = snake.popleft()
        board[tx][ty] = 0
    
    snake_p = nx
    snake_q = ny
        
     # 방향 전환
    if time in turns:
        if turns[time] == 'L':
            if direction == 0: # 현재 방향이 오른쪽이면, 위로 이동
                direction = 3
            elif direction == 1: # 현재 방향이 아래이면, 오른쪽으로 이동
                direction = 0
            elif direction == 2: # 현재 방향이 왼쪽이면, 아래로 이동
                direction = 1
            else: # 현재 방향이 위이면, 왼쪽으로 이동
                direction = 2
        else:
            if direction == 0: 
                direction = 1
            elif direction == 1: 
                direction = 2
            elif direction == 2: 
                direction = 3
            else: 
                direction = 0

print(time)