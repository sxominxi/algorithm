while True:
  li = list(map(int, input()))
  if li == [0]:
    break

  flag = "yes"
  for i in range(len(li)//2):
    if li[i] != li[-i-1]:
      flag = "no"
  print(flag)