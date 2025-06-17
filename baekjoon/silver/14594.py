import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
room = [0] * (N)
for m in range(M):
  x, y = map(int, input().split())
  for i in range(x-1, y-1):
    if room[i] == 0:
      room[i] = 1

print(room.count(0))