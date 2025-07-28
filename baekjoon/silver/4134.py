import sys, math
input = sys.stdin.readline

# 에라토스테네스의 체
# n 까지 숫자 나열
# 1 지우기
# 2, 3, 5, 7, 11, ..., 의 배수 지우기 
# 소수판정법에서 쓰는건 아니다. 어떤 범위 숫자의 소수를 알고싶을 때 쓰는 것. 
def prime(x):
  if x == 0 or x == 1:
    return False
  for i in range(2, int(math.sqrt(n))+1):
    if x % i == 0:
      return False
  return True

T = int(input())
for t in range(T): 
  n = int(input())
  while True:
    if prime(n):
      print(n)
      break
    else:
      n += 1