#손익분기점 판매량 공식 : 고정비 / 판매가 - 변동비
A, B, C = map(int, input().split())

count = 0

if C <= B:
    count = -1
else:
    count = A // (C - B) + 1

print(count)