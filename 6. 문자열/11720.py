count = int(input())
number = list(map(int, input()))
sum = 0

for i in range(0, count):
    sum += number[i]

print(sum)