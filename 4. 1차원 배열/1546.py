count = int(input())

score = list(map(int, input().split()))

M = max(score)

sum = 0
avg = 0

for i in score:
    sum += i / M * 100

avg = sum / count
print(avg)