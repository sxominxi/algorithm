import sys

N, M = map(int, sys.stdin.readline().split())

S = [str(sys.stdin.readline().strip()) for _ in range(N)]
arr = [str(sys.stdin.readline().strip()) for _ in range(M)]


cnt = 0
for i in arr:
    if i in S:
        cnt += 1
    else:
        continue
print(cnt)