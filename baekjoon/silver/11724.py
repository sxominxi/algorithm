import sys
input = sys.stdin.readline

def union(a, b):
  x = find(a)
  y = find(b)

  if x < y:
    parent[y] = x
  else:
    parent[x] = y

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
parent = [i for i in range(N + 1)]

for _ in range(M):
  u, v = map(int, input().split())
  union(u, v)

for i in range(1, N+1):
    find(i)

group_count = len(set(parent[1:]))  # 0번 노드는 제외
print(group_count)