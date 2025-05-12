import sys
input = sys.stdin.readline

# union
def union(a, b):
  # 부모를 찾아서 ?
  a = find(a)
  b = find(b)

  # 더 큰 쪽으로 ?
  if a != b:
    if a > b:
      route[b] = a
    else:
      route[a] = b
  
# find
def find(x):
  # 본인이 부모가 아니라면 ?
  if route[x] != x: 
    # 부모를 찾아서 저장해라 ?
    route[x] = find(route[x])
    
  return route[x]

T = int(input())
for t in range(T):
  N = int(input())
  P = list(map(int, input().split()))

  cycle = 0 # 사이클 개수
  route = [i for i in range(N)] # 부모 리스트 자기 자신으로 초기화

  for i in range(N):
    union(i, P[i]-1)

  for i in range(N): 
    find(i)

  print(len(set(route)))
