C = int(input())
avgLst = []

for i in range(0, C):
    score = list(map(int, input().split()))
    student = score[0]
    N = score[1: len(score)]
    scoreAvg = sum(N) / student
    memberAvg = len(list(filter(lambda score: score > scoreAvg, N))) / student * 100
    avgLst.append("{:.3f}%".format(memberAvg))

for avg in avgLst:
    print(avg)