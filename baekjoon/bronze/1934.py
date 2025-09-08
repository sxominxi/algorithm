import sys
input = sys.stdin.readline

T = int(input())

def Euclidean(a,b):
  while b != 0:
    r = a % b
    a = b
    b = r 
  return a

for tc in range(T):
  A, B = map(int, input().split())

  gcd = Euclidean(A, B)
  print(A*B//gcd)