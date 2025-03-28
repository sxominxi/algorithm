import sys
N = int(sys.stdin.readline())  # 숫자로 변환
li = [int(sys.stdin.readline().strip()) for _ in range(N)]  # 빠른 입력

li.sort(reverse=True)
i = int(N) -1
while i >= 0:
    print(li.pop()) 
    i -= 1