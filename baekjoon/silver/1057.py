arr = list(map(int, input().split()))

N = arr[0]
a = arr[1]
b = arr[2]

cnt = 0

while a != b:
  a -= a//2
  b -= b//2
  cnt += 1

print(cnt)