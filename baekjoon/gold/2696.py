import sys, heapq
input = sys.stdin.readline

T = int(input())
for tc in range(T):
  N = int(input())
  arr = []
  for _ in range(N // 10 + 1):
    arr += list(map(int, input().split()))

  left = [] # 최대 힙
  right = [] # 최소 힙
  ans = []
  for i, a in enumerate(arr):
    if not left or a <= -left[0]: # -를 붙이는 이유는, heap이 최소 값에 유리하기 때문
      heapq.heappush(left, -a)
    else:
      heapq.heappush(right, a)

    # 길이 맞추기: 최대 힙이 1개 더 많아야 함
    if len(left) > len(right) + 1:
      heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
      heapq.heappush(left, -heapq.heappop(right))

    if (i+1) % 2 == 1:
      ans.append(-left[0])

  print(len(ans))
  print(*ans)