def Cantoring(p, N):
  if N == 1:
    return
  
  for i in range(p + N//3, p + (N//3)*2):
    A[i] = ' '

  Cantoring(p, N//3)
  Cantoring(p + (N//3)*2, N//3)


while True:
  try:
    N = int(input())
    
    A = ['-']*(3**N)
    Cantoring(0, 3**N)
    print(''.join(A))

  except EOFError:
      break