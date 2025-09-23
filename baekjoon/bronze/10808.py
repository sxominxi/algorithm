S = list(input())

alp = [chr(c) for c in range(97, 123)]
ans = [0]*26

for s in S:
  ans[alp.index(s)] += 1

print(*ans)