import sys, heapq
input = sys.stdin.readline

N = int(input())
heap = []

for n in range(N):
  arr = map(int, input().split())

  for a in arr:
    if len(heap) < N:
      heapq.heappush(heap, a)
    else: # heap의 크기가 N과 같거나 클 때,
      if heap[0] < a: # 만약 heap에서 제일 작은 값이 a 보다 작다면
        heapq.heappop(heap) # heap에서 제일 작은 값을 빼고,
        heapq.heappush(heap, a) # a를 넣는다.

# 최종에서는 N개의 heap에서 제일 작은 값이 N번째 큰 수가 될 것.
print(heap[0])