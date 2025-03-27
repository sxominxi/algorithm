N = int(input())

# 몇번째 라인에 있는지 확인
line = 1
while N > line:
    N -= line
    line += 1 

# 라인이 짝수라면 분모가 줄어들음
if line % 2 == 0:
    up = N
    down = line - N + 1
# 라인이 홀수라면 분자가 줄어들음
else:
    up = line - N + 1
    down = N

print(f'{up}/{down}')