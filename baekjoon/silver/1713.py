import sys
input = sys.stdin.readline

N = int(input())  # 사진틀의 개수
total = int(input())  # 전체 학생 추천 횟수
recommend = list(map(int, input().split()))  # 추천받은 학생 리스트

dp = dict()      # 추천 횟수 저장
final = []       # 사진틀에 올라간 학생들
time = dict()    # 학생이 처음 올라온 시간 기록

for t, r in enumerate(recommend):  # 시간 정보 포함해서 순회
  if r in dp:
    dp[r] += 1  # 추천 수만 증가
  else:
    if len(final) >= N:
      # 후보 중 추천 수 가장 작고, 오래된 사람 제거
      target = min(final, key=lambda x: (dp[x], time[x]))
      final.remove(target)
      del dp[target]
      del time[target]
      
    dp[r] = 1
    time[r] = t
    final.append(r)

print(*sorted(final))