import sys

n = int(sys.stdin.readline().strip())

enter = set()
for _ in range(n):
    p = sys.stdin.readline().strip().split() 
    if p[1] == 'enter':
        enter.add(p[0])  
    else:
        enter.discard(p[0]) 

for name in sorted(enter, reverse=True):
    print(name)
