import sys
import heapq

input = sys.stdin.readline

heap = []
N = int(input())

for n in range(N):
  x = int(input())

  if x == 0 and heap:
    ans = heapq.heappop(heap)[1]
    print(ans)
  elif x == 0 and not heap:
    print(0)
  else:
    heapq.heappush(heap, (abs(x), x))