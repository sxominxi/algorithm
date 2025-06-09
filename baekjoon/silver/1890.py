import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# dp
dp = [[0]*N for _ in range(N)] 
dp[0][0]=1

for i in range(N):
  for j in range(N):
    k = int(grid[i][j])

    if k == 0 or dp[i][j] == 0: 
      continue # 해당 j 반복 넘기기 
    if i+k < N: # 아래쪽
      dp[i+k][j] += dp[i][j]
    if j+k < N: # 오른쪽 
      dp[i][j+k] += dp[i][j]

print(dp[-1][-1])