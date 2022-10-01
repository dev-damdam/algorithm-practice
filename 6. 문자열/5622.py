alphabet = list(input())
duration = 2

numbers = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"] 

sec = 0
for i in range(0, len(alphabet)):
    for j in range(0, len(numbers)):
        if numbers[j].find(alphabet[i]) >= 0:
            sec += duration + (j + 1)

print(sec)