razer = list(input())

stack = []
bar = 0

for i in range(len(razer)):
  if razer[i] == "(":
    stack.append('(')
  else:
    stack.pop()
    if razer[i-1] == "(":
      bar += len(stack)
    else:
      bar+= 1

print(bar)
