import sys
input = sys.stdin.readline

S = set()
M = int(input())
for _ in range(M):
  operation = list(map(str, input().split()))

  x = operation[0]

  if len(operation) == 2:
    y = int(operation[1])

  if x == 'add':
    S.add(y)
  elif x == 'remove':
    if y in S:
      S.remove(y)
  elif x == 'check':
    if y in S:
      print(1)
    else:
      print(0)
  elif x =='toggle':
    if y in S:
      S.remove(y)
    else:
      S.add(y)
  elif x ==  'all':
    S = set(i for i in range(1, 21))
  else:
    S = set()
    
