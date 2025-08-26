N = int(input())

def facto(n):
  ans = 1
  for i in range(2, n+1):
    ans *= i
  return ans

li = list(map(str, str(facto(N))))

cnt = 0
for i in range(len(li) - 1, -1, -1):
  if li[i] == "0":
    cnt += 1
  else:
    print(cnt)
    break
