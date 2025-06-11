import sys
input = sys.stdin.readline

N = int(input())

# 1보다 크거나 같고, 10^6보다 작거나 같은 정수
# dp에 저장되는 값은 연산횟수 
dp = [0]*1000001 

# 1은 아무것도 안해도 1이니까 건너뜀 (연산 0번)
for i in range(2, N+1):
  # 1을 빼는 연산
  dp[i] = dp[i - 1] + 1

  # 그러니까 일단 1을 빼는 연산을 저장해두고, 나누기들이랑 크기 비교 
  # 2로 나누어 떨어지면 비교해서 더 최소값 저장
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i // 2] + 1)

    # 3으로 나누어 떨어지면 비교해서 더 최소값 저장
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])