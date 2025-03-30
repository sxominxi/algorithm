N = int(input())

T = []
for n in range(0, N):
    T.append(list(map(int, input().split())))

T.sort(key=lambda x: (x[0], x[1]))

for i in range(0, N):
    print(*T[i])