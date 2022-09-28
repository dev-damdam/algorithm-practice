totalPrice = int(input())
count = int(input())
sum = 0

for i in range(0, count):
    product, price = map(int, input().split())
    sum += product * price

if totalPrice == sum:
    print("Yes")
else:
    print("No")