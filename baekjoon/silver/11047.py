import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = []
ans = 0
for _ in range(N):
  x = int(input())
  if x <= K:
    A.append(x)
  else:
    continue

while K > 0:
  ans += K // A[-1]
  K %= A[-1]
  A.pop()
  
print(ans)