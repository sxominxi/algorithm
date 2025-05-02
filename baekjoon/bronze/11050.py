import sys

N, M = map(int, sys.stdin.readline().split())

def facto(num):
  ans = 1
  while num > 1:
    ans *= num
    num -= 1
  return ans

print(round(facto(N) / (facto(N-M)*facto(M))))