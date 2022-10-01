#첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
word = list(input().lower())
tmpDict = {}

for alpha in word:
    if alpha in tmpDict:
        continue
    else:
        tmpDict[alpha] = word.count(alpha)

max = max(tmpDict.values())
resultLst = list(dict(filter(lambda el:el[1] == max, tmpDict.items())).keys())

if len(resultLst) == 1:
    print(resultLst[0].upper())
else:
    print("?")
