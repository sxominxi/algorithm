import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

d = dict()
for n in card:
    if n in d:
        d[n] += 1
    else:
        d[n] = 1

for m in check:
    if m in d:
        print(d[m], end=" ")
    else:
        print(0, end=" ")