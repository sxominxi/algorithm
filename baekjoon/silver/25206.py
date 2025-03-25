a = 0
cnt = 0
for n in range(0, 20):
    li = list(map(str, input().split()))

    if li[2] == 'P':
        continue
    else: 
        cnt += float(li[1])
        dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
        for k in dict.keys():
            if k == li[2]:
                a += dict[k]*float(li[1])
    
print('%.6f' % (a / cnt))
