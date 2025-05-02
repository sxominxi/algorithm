import sys

N = int(sys.stdin.readline())
divisor = list(map(int, sys.stdin.readline().split()))

if N == 1:
  print(divisor[0]**2)
else:
  print(min(divisor) * max(divisor))