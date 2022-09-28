#수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

numbers = []
result = []

# 입력
for i in range(10):
    numbers.append(int(input()) % 42)

for i in numbers:
    if i in result: continue
    else: result.append(i)

print(len(result))