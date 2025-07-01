import sys
input = sys.stdin.readline

def next_permutation(word):
    word = list(word)  # 문자열을 리스트로 변환
    i = len(word) - 2

    # 1️⃣ 뒤에서부터 앞을 탐색 → word[i] < word[i+1]인 지점 찾기
    while i >= 0 and word[i] >= word[i+1]:
        i -= 1

    if i == -1:
        return ''.join(word)  # 사전 순 마지막 순열이면 그대로 리턴

    # 2️⃣ 다시 뒤에서부터 → word[i]보다 큰 가장 작은 문자 찾기
    j = len(word) - 1
    while word[i] >= word[j]:
        j -= 1

    # 3️⃣ 둘을 교환
    word[i], word[j] = word[j], word[i]

    # 4️⃣ i+1 이후는 오름차순 정렬 (뒤집기)
    word[i+1:] = reversed(word[i+1:])

    return ''.join(word)

T = int(input())
for _ in range(T):
    word = input().strip()
    print(next_permutation(word))
