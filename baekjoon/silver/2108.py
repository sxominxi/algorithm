import sys

def f(arr):
  arr = set(arr)
  my_dict = {key : 0 for key in arr}

  for n in num:
    if n in my_dict:
        my_dict[n] += 1
  
    # 1. 가장 큰 빈도 구하기
  max_freq = max(my_dict.values())

  # 2. 가장 큰 빈도를 가진 key들만 리스트로 뽑기
  candidates = [k for k, v in my_dict.items() if v == max_freq]

  # 3. 정렬해서 두 번째로 작은 값 출력
  candidates.sort()
  if len(candidates) >= 2:
      print(candidates[1])
  else:
      print(candidates[0])

N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(N)]
num.sort()

print(round(sum(num)/N))
print(num[N//2])
f(num)
print(num[-1]-num[0])