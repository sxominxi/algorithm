import sys
input = sys.stdin.readline

n = int(input())

stack = []
ans = []
flag = True

i = 1
for _ in range(n):
  s = int(input())
  # 현재 입력 받은 수열보다 작은 수 push
  while i <= s:
    stack.append(i)
    ans.append('+')
    i += 1
  
  # 현재 입력 받은 수열과 같으면 pop 할 차례
  if stack[-1] == s:
    stack.pop()
    ans.append('-')
  # 이 경우엔 순서가 안맞음 될 수 없는 경우 => NO
  else:
    flag = False

if flag:
  for a in ans:
    print(a)
else:
  print('NO')