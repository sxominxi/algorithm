import sys

N = int(sys.stdin.readline())

hi = set()
cnt = 0
for _ in range(N):
  arr = str(sys.stdin.readline())

  if arr == 'ENTER\n':
    hi.clear()
    continue
  
  if arr not in hi:
    hi.add(arr)
    cnt += 1
  else:
    continue 

print(cnt)