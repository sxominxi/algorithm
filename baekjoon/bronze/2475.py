li = list(map(int, input().split()))

s = 0
for l in li:
  s += l**2

print(s%10)