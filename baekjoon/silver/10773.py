import sys

K = int(sys.stdin.readline())
stack = []

for _ in range(K):
    k = int(sys.stdin.readline())
    if k == 0:
        stack.pop()
    else:
        stack.append(k)

print(sum(stack))