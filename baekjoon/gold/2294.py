import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for _ in range(n):
  coin.append(int(input()))

dp = [[0]*n for _ in range(k)]

# for i in range(k):
#   for j in range(n):
    