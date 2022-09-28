A, B = map(int, input().split())

result = []
while A != 0 and B != 0:
    result.append(A + B)
    A, B = map(int, input().split())

for i in result:
    print(i)