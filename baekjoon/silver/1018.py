N, M = map(int, input().split())

board = []
ans = []
for _ in range(N):
    board.append(input())

for i in range(0, N-7):
    for j in range(0, M-7):
        b = 0 
        w = 0
        for p in range(i, i+8):
            for q in range(j, j+8):
                if (p + q) % 2 == 0:
                    if board[p][q] != 'B':
                        b += 1
                    if board[p][q] != 'W':
                        w += 1
              
                else:
                    if board[p][q] != 'W':
                        b += 1
                    if board[p][q] != 'B':
                        w += 1
        # 흰색으로 시작할 때 경우의 수
        ans.append(w)
        # 검은색으로 시작할 때 경우의 수
        ans.append(b)

print(min(ans))