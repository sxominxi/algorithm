import sys

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

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
plan = list(map(int, sys.stdin.readline().split()))

# 부모 초기화 -> 자기 자신
route = [i for i in range(N)]

for i in range(N):
  for j in range(N):
    # 이어져있는 도시이면, 유니온 해라
    if city[i][j] == 1:
      union(i, j)
  
for i in range(N): 
  find(i)

ans = 0
# print('route : ', route)
# 시작 지점
start = route[plan[0]-1]
for i in range(M):
  if route[plan[i]-1] != start:
    # ans = 'NO'
    continue
  else:
    # ans = 'YES'
    ans += 1

if ans == M:
  print('YES')
else:
  print('NO')