word = input().upper()
# 중복을 없애기 위해 set 한다음 list로 변환
word_list = list(set(word))

print(word_list)

cnt = []

for i in word_list:
  cnt.append(word.count(i))

print(cnt)

# 만약 max의 개수가 1개 초과라면 = 여러개 있다면 ? 출력
if cnt.count(max(cnt)) > 1:
  print("?")

# 아니라면 cnt가 max인 idx를 이용하여 출력
else:
  print(word_list[(cnt.index(max(cnt)))])