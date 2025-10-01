N, K = map(int, input().split())

queue = [i+1 for i in range(N)]
pop = K-1
ans = []

while queue:
  ans.append(queue.pop(pop))
  pop += K-1
  if pop >= len(queue) and queue:
    pop %= len(queue)

print("<" + ", ".join(map(str, ans)) + ">")