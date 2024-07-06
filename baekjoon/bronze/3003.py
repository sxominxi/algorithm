piece = list(map(int, input().split()))

ans = [0]*6

for i in range(6):
  if i == 0 or i == 1:
    a = piece[i] - 1
    ans[i] = -a

  if i == 2 or i == 3 or i == 4:
    b = piece[i] - 2
    ans[i] = -b

  if i == 5:
    c = piece[i] - 8
    ans[i] = -c

print(*ans)
  