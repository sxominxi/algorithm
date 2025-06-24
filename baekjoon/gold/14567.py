import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range (N+1)] # 선수과목에 조건과목 저장
indegree = [0 for _ in range (N+1)] # 과목의 차수 저장
answer = [1 for _ in range (N+1)] # 답

for _ in range(M):
  A, B = map(int, input().split())
  arr[A].append(B)
  indegree[B] += 1 # B과목 차수 높이기 

dq = deque()
for i in range(1, N+1):
  if indegree[i] == 0: # i과목의 차수가 0이면, 이수조건이 없다는 뜻
    dq.append(i)

while dq:
  x = dq.popleft()
  for a in arr[x]: # x과목에 대하여 이제 들을 수 있는 강의 중, 
    indegree[a] -= 1 # x과목 수강했으니 차수 빼줌 
    if indegree[a] == 0: # 만약 차수가 0이 되면 수강 할 수 있음
      answer[a] = answer[x] + 1 # x과목의 수강회수에 + 1을 해줌
      dq.append(a) # 이제 a과목의 다음 과목을 탐색

print(*answer[1:])