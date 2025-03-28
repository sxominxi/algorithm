n = int(input()) 

cnt = 0 
# n이 0보다 작아지면 else문 실행행
while n>=0: 
    # n이 5로 나눠지면 5 카운트, 0이 될거니까 break
    if n%5==0:
        cnt += (n//5) 
        print(cnt)
        break
    # 5로 안나눠지면 3 카운트트
    n -= 3 
    cnt += 1
else:
    print(-1) 