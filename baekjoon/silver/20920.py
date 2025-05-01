import sys

N, M = map(int, sys.stdin.readline().split())

hwaen = dict()
for _ in range(N):
  word = str(sys.stdin.readline().strip())
  if len(word) < M:
    continue
  else:
    if word not in hwaen:
      hwaen[word] = 1
    else:
      hwaen[word] += 1

hwaen = sorted(hwaen.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for h in hwaen:
  print(h[0])