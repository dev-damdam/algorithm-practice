#N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

N = int(input())
numbers = list(map(int, input().split()))

max = numbers[0]
min = numbers[0]
for i in numbers:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min, max)
# print(min(numbers), max(numbers))