T = int(input())
result = []

for i in range(0, T):
    R, S = map(str, input().split())
    R = int(R)

    tmpLst = list(S)
    tmpStr = ""
    
    for i in range(0, len(tmpLst)):
        tmpStr += tmpLst[i] * R
    
    result.append(tmpStr)

for i in result:
    print(i)