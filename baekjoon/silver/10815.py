import sys

N = int(sys.stdin.readline())
sgcard = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

for m in card:
    if m in sgcard:
        print(1, end=" ")
    else:
        print(0, end=" ")
