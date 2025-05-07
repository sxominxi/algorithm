import sys
import heapq

# V : 정점의 개수 / E : 간선의 개수
V, E = map(int, sys.stdin.readline().split())
# K : 시작 정점
K = int(sys.stdin.readline())

# 인접리스트
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))  # u에서 v로 가는 가중치 w


def dijkstra(graph, start):
  distance = [float('inf')] * (V+1)
  distance[start] = 0
  heap = []
  heapq.heappush(heap, (0, start))

  while heap:
    # 우선순위가 가장 낮은 값(가장 작은 거리)
    dist, now = heapq.heappop(heap)

    # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 넘어간다
    if distance[now] < dist:
      continue

    for v, w in graph[now]:
      # 기존에 입력되어있는 값보다 크다면
      if dist + w < distance[v]:
        distance[v] = dist + w
        heapq.heappush(heap, (dist + w, v))
  
  return distance

distances = dijkstra(graph, K)

# 출력
for i in range(1, V + 1):
    print(distances[i] if distances[i] != float('inf') else 'INF')