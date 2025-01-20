N = int(input())
cnt = 0

plag = True
for n in range(0, N):
    w = set(input())
    
    if len(w) == 1:
        cnt += 1
        break

    else:
        for word in w:
            idx = []
            for i in range(len(N)):
                if N[i] == word:
                    idx.append(i)
            for j in range(len(idx)-1):
                plag = False
                break
        
        if plag == True:
            cnt += 1

print(cnt)