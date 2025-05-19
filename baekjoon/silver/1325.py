import sys
input = sys.stdin.readline

N,M = map(int, input().split())
trust = [[] for _ in range(N+1)]

for _ in range(M):
  A,B = map(int, input().split())
  trust[B].append(A)

def dfs(x, visited):
  visited[x] = 1
  cnt = 1
  for node in trust[x]:
    if not visited[node]:
      cnt += dfs(node,visited)
  return cnt

ans = []
for i in range(1, N+1):
  visited = [0]*(N+1)
  ans.append(dfs(i,visited))

for a in len(ans):
  if ans[a] == max(ans):
    print(a, end=' ')

# for i in range(N+1):
#   x = trust[i]

#   for j in x:
#     y = trust[j]
#     if y :
#       trust[i].extend(y) 여기서 메모리 초과..
#     else:
#       continue

# max_len = max(len(lst) for lst in trust)
# result = [i for i in range(len(trust)) if len(trust[i]) == max_len]
# print(*result)