# 피리 부는 사나이

# 반드시 통과하게 되는 최소 지점 찾기
# 사이클 개수를 찾으면 되겠구나 = 사이클 판별 레쓰고
# 사이클 판별 DFS 이용
def findCycle(start):
  global count
  visited[start] = 1 # 방문 체크
  node = graph[start] # 방문 할 노드
  if not visited[node]: # 아직 방문 안했으면 함수 돌리기 ㄱ ㄱ
    findCycle(node)
  elif not finished[node]: # 만약 이동이 끝나지 않았다면 -> 사이클 체크
    count += 1
  finished[start] = 1 # 함수 한바퀴 다 돌면 이동 완료 체크

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dir = []
for _ in range(N):
  line = input().strip()
  dir.extend(list(line))

graph = [0] * (N*M)
visited = [0] * (N*M)
finished = [0] * (N*M)
count = 0

# 매핑 어캐하지 ..
# 방향 한 줄로 변환해서 양방향 매핑 함 <- 실패 요인
# 왔다갔다 하는게 아닌데 왜 양방향 매핑함 ?? 단방향이어야함 
for i in range(N*M):
    if dir[i] == 'D':
        graph[i] = i + M
    elif dir[i] == 'U':
        graph[i] = i - M
    elif dir[i] == 'R':
        graph[i] = i + 1
    else:  # 'L'
        graph[i] = i - 1

for i in range(N*M):
    # if not visited[i]:
        findCycle(i)

print(count)