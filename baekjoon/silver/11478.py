import sys

S = sys.stdin.readline().strip()
# 부분문자열 중복없이 세트로 만들기
substr = set()

# 부분부분 다 끊어서 넣기, 어차피 세트라 중복은 제거됨 (순서까지 같아야 중복이라고 봄봄)
# 부분 문자열은 S에서 연속된 일부분을 말하기 때문에 가능
for i in range(len(S)):
    for j in range(1+i, len(S)+1):
        substr.add(S[i:j])

print(len(substr))
