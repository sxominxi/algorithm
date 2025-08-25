# T = int(input())

# for t in range(T):
#   H, W, N = map(int, input().split())

#   stair = N % H
#   if stair == 0:
#     stair = H

#   ho = (N - 1) // H + 1

#   print(f"{stair}{ho:02d}")  

# 다른 풀이

T = int(input())

for t in range(T):
  H, W, N = map(int, input().split())

  stair = N % H * 100
  ho = N // H + 1

  if N % H == 0:
    stair = H * 100
    ho = N // H

  print(stair+ho)