import sys
input = sys.stdin.readline

# DFS로 사이클 확인 
def findCycle(start):
  for node in graph[start]:
    # 시작노드에서 부모노드 방문 제외 (부모->자식 방향)
    if parent[start] == node:
      continue

    # 근데 방문처리가 된 곳에 방문하게 되면 그 곳은 사이클 
    if visited[node]:
      return True
    
    # 재귀
    parent[node] = start
    visited[node] = 1
    if findCycle(node):
      return True
  
  # 모든 조건을 패스하면 사이클 없는 것
  return False

n, m = map(int, input().split())
case = 1

while n != 0 or m != 0:
    graph = [[] for _ in range(n+1)]
    parent = [-1]*(n+1)
    visited = [0]*(n+1)
    count = 0
    
    # 양방향 매핑
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # visited가 0인 모든 노드를 돌면서
    # 가능한 모든 연결 요소(연결 그래프)를 순회함
    for node in range(1, n+1):
        if visited[node] == 0:
            # 처음에는 자기 자신을 부모로 초기화
            parent[node] = node
            visited[node] = 1
            if not findCycle(node):
                count += 1
    
    if count == 0:
        print(f'Case {case}: No trees.')
    elif count == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {count} trees.')
    
    case += 1
    n, m = map(int, input().split()) 
