import sys
input = sys.stdin.readline

def factorial(n):
  ans = 1
  while n > 1:
    ans *= n
    n -= 1
  return ans

T = int(input())
for t in range(T):
  N, M = map(int, input().split())

  # 조합 mCn
  print(factorial(M)//(factorial(N)*factorial(M-N)))