# 인풋 받기
N = int(input())

cnt = 0

for n in range(N):
    # 문자별로 받기
    word = list(input())
    # 중복 제거 리스트
    set_word = list(set(word))

    flag = True

    for w in set_word:
         # 각 문자의 인덱스 저장하기
        idx = []

        for i in range(len(word)):
            if word[i] == w:
                idx.append(i)

        # 인덱스가 이어지는지 확인
        # 근데 idx의 길이만큼 돌리면 마지막 자리에서 에러나니까 -1
        for j in range(len(idx)-1):
            # 만약 인덱스가 이어지지 않는다면 False를 저장하고 끝내기기
            if (idx[j] + 1) != idx[j+1]:
                flag = False
                break
            # 이어진다면 True 유지
            else:
                continue
                
    # 단어를 전부 돌았을때도 True가 유지되었다면 개수를 세준다다
    if flag == True:
        cnt += 1

print(cnt)