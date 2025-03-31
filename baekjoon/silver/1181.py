N = int(input())

word = []
for n in range(0, N):
    word.append(str(input()))

word = list(set(word))
word.sort(key=lambda x : [len(x), x])
print('\n'.join(word))