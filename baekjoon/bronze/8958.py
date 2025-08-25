T = int(input())

for t in range(T):
  li = list(map(str, input()))

  s = 1
  score = 0
  for l in li:
    if l == "O":
      score += s
      s += 1
    else:
      s = 1
  print(score)