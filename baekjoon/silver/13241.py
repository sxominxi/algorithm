import sys
input = sys.stdin.readline

A, B = map(int, input().split())
C = A * B

while B:
  if A > B:
    A, B = B, A
  B %= A

print(C//A)