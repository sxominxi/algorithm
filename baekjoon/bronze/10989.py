import sys
input = sys.stdin.readline

N = int(input())
cnt = [0] * 10001 # 1부터 10000까지의 숫자를 저장할 배열

for _ in range(N):
  num = int(input())
  cnt[num] += 1 # 입력받은 숫자를 카운팅해준다 

for i in range(10001):
  if cnt[i] != 0: # 숫자를 입력받은 적이 있다면, 
    for j in range(cnt[i]): # 입력받은 만큼 그 수를 출력 
      print(i)