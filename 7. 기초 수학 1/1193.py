line = 0
end = 0

N = int(input())

while N > end:
    line += 1
    end += line

diff = end - N
top = 0
bottom = 0

if line %2 == 0: #짝수 라인
    top = line - diff
    bottom = diff + 1
else: #홀수 라인
    top = diff + 1
    bottom = line - diff

print("%d/%d" % (top, bottom))
