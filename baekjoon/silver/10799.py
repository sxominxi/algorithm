razer = list(input())
stack = []
ans = 0

for i in range(len(razer)):
  if razer[i] == "(":
    stack.append("(")
  else:
    stack.pop()
    if razer[i-1] == ")":
      ans += 1
    else:
      ans += len(stack)
print(ans)