s = str(input())
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for alp in a:
    s = s.replace(alp, '*') 

print(len(s))