import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

P = sorted(P)
for i in range(1, len(P)):
  P[i] = sum(P[i-1:i+1])
print(sum(P))