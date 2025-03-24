N = int(input())

cnt = 0
for n in range(0, N):
    word = list(map(str, input()))
    word_set = list(set(word))
    
    # 1. word와 word_set 알파벳 비교
    # 2. 같으면 다음 인덱스 체크 > 반복
    # 3. 다음 인덱스에 다른 알파벳이 나오면 word_set에서 *으로 변경
    # 4. word_set에 없는 알파벳이 word에서 나오면 break, false 처리
    # 5. 문제 없으면 cnt += 1
    
    flag = True
    i = 0
    while i < len(word):
        if word[i] not in word_set:
                flag = False
                break
        else:
            j = 0
            while j < len(word_set):
                if word[i] != word_set[j]:
                    j += 1
                    continue
                else:
                    if i < len(word)-1:
                        if word[i+1] != word_set[j]:
                            word_set[j] = '*' 
                j += 1
                    
            i += 1

    if flag == True:
        cnt += 1

print(cnt)