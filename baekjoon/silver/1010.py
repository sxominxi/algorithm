def facto(N):
  ans = 1
  while N > 1:
    ans *= N
    N -= 1
  return ans

import sys

T = int(sys.stdin.readline())

for _ in range(T):
  N, M = map(int, sys.stdin.readline().split())

  if M == N:
    print(1)
  else:
    print(round(facto(M) / (facto(M-N)*facto(N))))