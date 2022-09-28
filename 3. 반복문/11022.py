import sys

count = int(sys.stdin.readline())

result = []

for i in range(0, count):
    a, b = map(int, sys.stdin.readline().split())
    result.append("%d + %d = %d" % (a, b, a + b))

for i in range(0, len(result)):
    print("Case #%d: %s" % (i + 1, result[i]))