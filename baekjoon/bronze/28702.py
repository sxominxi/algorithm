li = [input() for _ in range(3)]

for i in range(3):
  if li[i] != "Fizz" and li[i] != "Buzz" and li[i] != "FizzBuzz":
    idx = i
    num = int(li[i])
    break

ans = num+(3-idx)
if ans % 3 == 0 and ans % 5 == 0:
  print("FizzBuzz")
elif ans % 3== 0 :
  print("Fizz")
elif ans % 5 == 0:
  print("Buzz")
else:
  print(ans)