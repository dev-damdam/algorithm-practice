#10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.

def generate_number(n):
    n = n + sum(map(int, str(n)))
    return n

generater = []

for n in range(1, 10001):
    generater.append(generate_number(n))

for n in range(1, 10001):
    if n not in generater:
        print(n)