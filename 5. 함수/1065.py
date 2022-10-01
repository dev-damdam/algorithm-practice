def getHansuCount(n):
    count = 0
    if n < 100: 
        count = n
    else:
        count = 99
        for i in range(100, n + 1):
            num1 = i // 100
            num2 = i % 100 // 10
            num3 = i % 100 % 10
            if num2 - num1 == num3 - num2:
                count += 1
    return count

N = int(input())
hansuCount = getHansuCount(N)
print(hansuCount)

