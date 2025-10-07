def Euclidean(a,b):
  while b != 0:
    r = a % b
    a = b
    b = r
  return a
  
a, b = map(int, input().split())

gcd = Euclidean(a, b)
print(gcd)
print(a*b//gcd)