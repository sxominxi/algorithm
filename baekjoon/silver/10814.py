N = int(input())

li = []
for n in range(N):
    age, name = map(str, input().split())
    li.append([int(age), name])

li.sort(key=lambda x : (x[0]))
for n in range(N):
    print(*li[n])