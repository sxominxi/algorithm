import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

row = 0
while row < N:
  min_route = min(arr[row])
  