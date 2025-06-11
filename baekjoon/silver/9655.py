import sys
input = sys.stdin.readline

N = int(input())

dp = [-1]*1001 # N이 1000 까지

# 0이 창영, 1이 상근 
dp[1] = 1 # 상근이 먼저 시작
dp[2] = 0
dp[3] = 1

for i in range(4, N+1): # 1 ~ 3은 저장해둠
  if dp[i-1] == 1 or dp[i-3] == 1: # 1개 전이나 3개 전이 상근이면,
    dp[i] = 0 # 찬영이 이김
  else:
    dp[i] = 1

if dp[N] == 1:
  print('SK')
else:
  print('CY')