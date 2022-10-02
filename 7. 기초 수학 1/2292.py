N = int(input())

start = 1
end = 1
count = 1

while N > end:
    start = end + 1
    end = start + 6 * count - 1
    count += 1

print(count)