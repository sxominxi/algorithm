import sys
input = sys.stdin.readline

R, C = map(int, input().split())
farm = [list(map(str, input().strip())) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

possible = True

for i in range(R):
    for j in range(C):
        if farm[i][j] == 'W':  # 늑대 주변 체크
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < R and 0 <= nj < C:
                    if farm[ni][nj] == 'S':
                        possible = False  # 바로 옆에 양이 있으면 안 됨
                        break
                    elif farm[ni][nj] == '.':
                        farm[ni][nj] = 'D'  # 울타리 설치
            if not possible:
                break
    if not possible:
        break

if possible:
    print(1)
    for row in farm:
        print(''.join(row))
else:
    print(0)