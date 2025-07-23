N = int(input())
tree = []

for _ in range(N):
  x = int(input())
  tree.append(x)

sub =[]
for i in range(N-1):
  d = tree[i+1] - tree[i]
  sub.append(d)

def gcd(a, b):
  while b > 0:
    a, b = b, a%b
  return a

ans = sub[0]
for i in range(1, N-1):
  ans = gcd(ans, sub[i])

cnt = 0
for i in sub:
  cnt += i // ans - 1

print(cnt)