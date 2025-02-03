input = list(map(int, input().split()))
output = [0, 0, 0, 0, 0, 0]

output[0] = 1 - input[0] 
output[1] = 1 - input[1] 
output[2] = 2 - input[2] 
output[3] = 2 - input[3] 
output[4] = 2 - input[4] 
output[5] = 8 - input[5] 

print(*output)