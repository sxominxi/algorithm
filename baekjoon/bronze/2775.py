T = int(input())

for t in range(T):
  k = int(input())
  n = int(input())

  li = [i for i in range(1, n+1)]

  for i in range(k):
    for j in range(n):
      flag = 0
      num = 0
      while flag <= j:
        num += li[i*n+flag]
        flag += 1
      li.append(num)

  print(li[-1]) 