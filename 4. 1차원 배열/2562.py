numbers = []

# 입력
for i in range(9):
    numbers.append(int(input()))

max = numbers[0]
maxIdx = 0

for i in range(9):
    if numbers[i] >= max:
        max = numbers[i]
        maxIdx = i + 1

print(max)
print(maxIdx)

# print(max(numbers))
# print(numbers.index(max(numbers)) + 1)