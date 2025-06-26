import sys  
input = sys.stdin.readline  
from collections import deque  

def bfs(ci, cj):  
    q = deque()  
    q.append((ci, cj))  
    while q:  
        si, sj = q.popleft()  

        # 에어컨에 대해서 4방향 탐색하며  
        # 한 방향에 대해서는 while문을 통해 이동        
        for d in range(4):  
            # 방향 전환 위하여 현재 이동 방향 따로 기록해주기  
            dx, dy = di[d], dj[d]  
            ni, nj = si + dx, sj + dy  
            while 0<=ni<N and 0<=nj<M:  
                visited[ni][nj] = 1  
                # 에어컨 만나면 종료 -> 중복 방문하기 때문에  
                if arr[ni][nj] == 9:  
                    break  
                # 벽은 만나는 경우 체크해주어야 하는데  
                # 3번 벽은 -> 아래로 가면 왼쪽으로 전환, 왼쪽으로 가면 아래로 전환                
                #             즉, 1, 0 에서 -1, 0으로 -1, 0에서 0, 1로 변경                
                #             => dx, dy = -dy, -dx로 변경해주면 된다.                
                # 4번 벽은 -> 아래로 가면 오른쪽, 오른쪽으로 가면 아래로 전환                
                #              1, 0에서 0, 1로 0,1에서 1,0이므로           
                #              => dx, dy = dy, dx                
                # 1번 벽의 경우 왼쪽 오른쪽 이동 중 1번 벽을 만나면 왔던 길을 돌아가므로 종료,                
                # 2번도 위아래 이동 중 만나면 종료                
                if arr[ni][nj] == 3:  
                    dx, dy = -dy, -dx  
                elif arr[ni][nj] == 4:  
                    dx, dy = dy, dx  
                elif arr[ni][nj] == 1 and dx == 0:  
                    break  
                elif arr[ni][nj] == 2 and dy == 0:  
                    break  

                ni += dx  
                nj += dy  

N, M = map(int, input().split())  
arr = [[*map(int, input().split())] for _ in range(N)]  
air_conditional = []  
for i in range(N):  
    for j in range(M):  
        if arr[i][j] == 9:  
            air_conditional.append((i, j))  

di, dj = [1, -1, 0, 0], [0, 0, 1, -1]  
visited = [[0] * M for _ in range(N)]  
for i, j in air_conditional:  
    visited[i][j] = 1  
    bfs(i, j)  

result = 0  
for i in visited:  
    result += i.count(1)  
print(result)