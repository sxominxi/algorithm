N,B=map(int,input().split())

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ans = []
while N > 0:
    a = digits[N % B]
    ans.append(a) 
    N = N // B  

ans.reverse()
print("".join(ans))