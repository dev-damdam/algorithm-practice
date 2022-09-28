import sys

count = int(sys.stdin.readline())

result = []

for i in range(0, count):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d" % (i + 1, a + b))