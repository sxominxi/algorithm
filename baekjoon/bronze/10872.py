import sys

N = int(sys.stdin.readline())
ans = 1
while N > 1:
  ans *= N
  N -= 1
print(ans)