N = int(input())

li = list(map(int, input().split()))
T, P = map(int, input().split())

t = 0
for l in li:
  if l == 0:
    continue
  if l % T == 0:
    t += l // T
  else:
    t += l // T + 1

p = N // P       
r = N % P  

print(t)
print(p, r)