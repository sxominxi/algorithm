import sys
input = sys.stdin.readline

M, N = map(int, input().split())

is_prime = [1]*(N+1)
is_prime[0] = is_prime[1] = 0

i = 2
while i*i <= N:
  if is_prime[i]:
    j = i*i
    while j <= N:
      is_prime[j] = 0
      j += i
  i += 1

out = []
for x in range(M, N + 1):
    if is_prime[x]:
        out.append(str(x))

sys.stdout.write("\n".join(out))