T = int(input())

li = []
for t in range(T):
  x, y = map(int, input().split())
  li.append((x, y))

ranks = [1]*T
for i in range(T):
  for j in range(T):
    if i == j:
      continue

    if li[j][0] > li[i][0] and li[j][1] > li[i][1]:
      ranks[i] += 1

print(*ranks)