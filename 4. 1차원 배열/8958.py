count = int(input())

quiz = []
totalScore = []
# 입력
for i in range(0, count):
    quizResult = list(input())
    count = 0
    score = 0

    for j in quizResult:
        if j == "O":
            count += 1
        else:
            count = 0
        score += 1 * count
    totalScore.append(score)

for score in totalScore:
    print(score)