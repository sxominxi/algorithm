import sys
N, M = map(int, sys.stdin.readline().split())

poketmon = {n+1: str(sys.stdin.readline().strip()) for n in range(N)}
inverse_poketmon = {v:k for k,v in poketmon.items()}
quiz = [str(sys.stdin.readline().strip()) for _ in range(M)]

for q in quiz:
    if q.isdigit():
        print(poketmon[int(q)])  
    else:
        print(inverse_poketmon[q]) 