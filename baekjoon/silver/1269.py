import sys
A, B = map(int, sys.stdin.readline().split())
listA = list(map(int, sys.stdin.readline().split()))
listB = list(map(int, sys.stdin.readline().split()))

setAB = set(listA + listB)
AB = setAB - set(listA) 
BA = setAB - set(listB)

print(len(AB) + len(BA))