# DNA 해독

N = int(input())
arr = list(str(input()))

while len(arr) > 1:
  n = arr.pop(-1)
  n_1 = arr.pop(-1)

  if n == 'T':
    if n_1 == 'A':
      arr.append('G')
    elif n_1 == 'G':
      arr.append('A')
    elif n_1 == 'C':
      arr.append('G')
    else:
      arr.append('T')

  elif n == 'C':
    if n_1 == 'A':
      arr.append('A')
    elif n_1 == 'G':
      arr.append('T')
    elif n_1 == 'C':
      arr.append('C')
    else:
      arr.append('G')

  elif n == 'G':
    if n_1 == 'A':
      arr.append('C')
    elif n_1 == 'G':
      arr.append('G')
    elif n_1 == 'C':
      arr.append('T')
    else:
      arr.append('A')

  else:
    if n_1 == 'A':
      arr.append('A')
    elif n_1 == 'G':
      arr.append('C')
    elif n_1 == 'C':
      arr.append('A')
    else:
      arr.append('G')

print(*arr)