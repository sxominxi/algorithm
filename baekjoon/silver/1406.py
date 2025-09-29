import sys
input=sys.stdin.readline

left=list(str(input().strip()))
right=[]
M=int(input())

for m in range(M):
  order=list(map(str,input().split()))

  if order[0] == "L" and left:
    right.append(left.pop())
  elif order[0] == "D" and right:
    left.append(right.pop())
  elif order[0] == "B" and left:
    left.pop()
  elif order[0] == "P":
    left.append(order[1])

right.reverse()
ans=left+right
print("".join(ans))