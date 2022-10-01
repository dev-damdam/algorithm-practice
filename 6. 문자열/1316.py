#첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

N = int(input())
groupWordCount = N
for i in range(0, N):
    word = input()
    for j in range(0, len(word) - 1):
        if word[j] == word[j + 1]:
            pass
        elif word[j] in word[j+1::]:
            groupWordCount -= 1
            break
print(groupWordCount)