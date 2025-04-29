import sys

N = int(sys.stdin.readline())
dance = set()
dance.add('ChongChong')

for _ in range(N):
  x, y = map(str, sys.stdin.readline().split())

  if x in dance or y in dance:
    dance.add(x)
    dance.add(y)

print(len(dance))