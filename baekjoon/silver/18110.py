import sys
input = sys.stdin.readline

def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

N = int(input())

if N == 0:
  print(0)
else:
  ex = roundUp(N*0.15)

  op = []
  for n in range(N):
    op.append(int(input()))

  op.sort()
  print(roundUp(sum(op[ex:N-ex])/len(op[ex:N-ex])))