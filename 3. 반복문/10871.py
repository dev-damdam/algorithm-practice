N, X = map(int, input().split())

numbers = map(int, input().split())

result = []

for i in numbers:
    if X > i:
        print("%d" % i, end=" ")
