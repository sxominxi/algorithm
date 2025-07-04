import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [1]*N

for i in range(1, N):
  for j in range(i):
    # 앞 선 수들보다 큰지 확인 
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))