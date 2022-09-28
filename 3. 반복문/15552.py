import sys

count = int(sys.stdin.readline().rstrip())

result = []

for i in range(0, count):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)