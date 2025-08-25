A = int(input())
B = int(input())
C = int(input())

N = A * B * C
li = list(map(int, str(N)))

ans = [0]*10

for l in li:
  ans[l] += 1

for a in ans:
  print(a)