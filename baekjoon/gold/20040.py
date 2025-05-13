# 사이클 게임

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # 경로 압축
        x = parent[x]
    return x

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root == y_root:
        return False  # 사이클 발생
    parent[y_root] = x_root
    return True

import sys
input = sys.stdin.readline

ans = 0
n, m = map(int, input().split()) # n = 점의 개수 / m = 진행 차레
parent = [i for i in range(n)]

for i in range(m):
  a, b = map(int, input().split()) # 선택한 점 두 개  
  if not union(a, b):
    if ans == 0:
      ans = i+1  # 사이클이 처음 발생한 차례

print(ans)