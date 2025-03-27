a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

flag = 0
if a1 * n0 + a0 <= c * n0 and a1 * 100 + a0 <= c * 100:
    flag = 1


print(flag)