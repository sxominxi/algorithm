import sys

N, M = map(int, sys.stdin.readline().split())
nosee = set(str(sys.stdin.readline().strip()) for _ in range(N))
no = set()
for m in range(M):
    noheard = str(sys.stdin.readline().strip())
    if noheard in nosee:
        no.add(noheard)
no = sorted(list(no))
print(len(no), end="\n")
for n in no:
    print(n)