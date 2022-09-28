#26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다

N = int(input())
newN = N

count = 0

while True:
    count += 1
    quotient = newN // 10
    remainder = newN % 10
    sum = quotient + remainder
    newN = remainder * 10 + (sum % 10)
    if N == newN: break
    else: continue

print(count)
