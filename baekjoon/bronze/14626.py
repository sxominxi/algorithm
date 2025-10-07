ISBN = list(map(str, input()))

sum = 0
for i in range(len(ISBN)):
  if ISBN[i] == "*":
    idx = i
  else:
    if i % 2 == 0:
      sum += int(ISBN[i])
    else:
      sum += 3*int(ISBN[i])

if idx % 2 == 0:
  ans = 10 - sum%10
  print(ans)
else:
  for ans in range(10):
    if (ans*3 + sum) % 10 == 0:
        print(ans)
        break
