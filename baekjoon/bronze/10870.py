N = int(input()) # 입력받기

def fibo(n): # 피보나치 함수
  if n < 2: # 1번째 피보나치 수 까지는
    return n # 그대로 반환환
  else: # 그 이후부터는 
    return fibo(n-1) + fibo(n-2) # 바로 앞 두 피보나치 수의 합을 return

print(fibo(N))