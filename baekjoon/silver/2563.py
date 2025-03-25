N = int(input())
cnt = 0
do = [[0]*100 for _ in range(100)]
for n in range(0, N):
    A, B = map(int, input().split())

    for i in range(0, 10):
        for j in range(0, 10):
            do[B+i][A+j] = 1


for i in range(0, 100):
    for j in range(0, 100):
        if do[i][j] == 1:
            cnt += 1
print(cnt)