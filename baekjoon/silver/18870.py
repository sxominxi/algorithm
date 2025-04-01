import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

setarr = sorted(list(set(arr)))

dic = {setarr[i] : i for i in range(len(setarr))}
for i in arr:
    print(dic[i], end = ' ')