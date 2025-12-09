import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = dict()
for _ in range(N):
  site, password = map(str, input().split())
  d[site] = password

for _ in range(M):
  x  = str(input().strip())
  print(d[x])