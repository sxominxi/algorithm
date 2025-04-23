from collections import deque

n = int(input())
balloons = list(map(int, input().split()))

# 풍선 번호와 이동 값을 함께 저장
q = deque((i + 1, num) for i, num in enumerate(balloons))
result = []

while q:
    index, move = q.popleft()
    result.append(index)

    if move > 0:
        q.rotate(-(move - 1))  # 오른쪽으로 (move - 1)칸 이동
    else:
        q.rotate(-move)        # 왼쪽으로 move칸 이동 (음수니까 -move는 양수)

print(' '.join(map(str, result)))
