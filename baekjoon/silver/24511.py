import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

ans = []
cnt = 0
while cnt < M:
  x = []
  for i in range(N):
    # turn 시작할때
    if i == 0:
      if A[i] == 0: # 큐
        x.append(B[i])
        B[i] = C[cnt]   
      else: # 스택
        x.append(C[cnt])

    else:
      if A[i] == 0: # 큐
        x.append(B[i])
        B[i] = x[i-1]
      else: # 스택
        x.append(x[i-1])  
    
  ans.append(x[-1]) 
  cnt += 1
print(*ans)