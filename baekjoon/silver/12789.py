import sys

N = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))

wating = []
success = []

i = 1
j = 0
while i <= N and j <= N:
    if wating:
        if wating[-1] == i:
            success.append(i)
            wating.pop()
            i += 1
            continue

    if j < N:
        if line[j] == i:
            wating.append(line[j])
        else:
            wating.append(line[j])
    j += 1
  

if len(success) == N:
    print('Nice')
else:
    print('Sad')