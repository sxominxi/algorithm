import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

A_set = set(A)

for n in nums:
  if n in A_set:
    print(1)
  else:
    print(0)