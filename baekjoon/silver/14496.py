import sys 
from collections import deque
input = sys.stdin.readline

def bfs(x):
    q = deque()
    q.append((x, 0))  # (노드, 거리)
    visited[x] = 1

    while q:
        cur, dist = q.popleft()
        if cur == b:
            return dist
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = 1
                q.append((next, dist + 1))
    return -1

a, b = map(int, input().split())
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]  
visited = [0]*(N+1)              

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(a))
