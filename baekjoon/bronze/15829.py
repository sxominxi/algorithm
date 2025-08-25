L = int(input())
li = list(map(str, input()))

h = 0
for i in range(L):
  num = ord(li[i]) - 96
  h += num*(31**i)

print(h % 1234567891)