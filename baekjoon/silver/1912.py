import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N
dp[0] = arr[0] # 0번 인덱스 까지의 최대합은 arr[0]

for i in range(1, N):
  dp[i] = max(arr[i], dp[i-1]+arr[i]) # 이전까지의 합이 더 크면 더한거, 아니면 새로

print(max(dp))