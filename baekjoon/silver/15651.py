import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [0] * (N+1)
seq = []

def back():
  if len(seq) == M:
    print(*seq)
    return
  
  for i in range(1, N+1):
    seq.append(i)
    print('seq = ',seq)
    back()
    seq.pop()

back()