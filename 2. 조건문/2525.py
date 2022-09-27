A, B = map(int, input().split())
C = int(input())

hours = (B + C) // 60
minutes = (B + C) % 60

if hours > 0:
    A = A + hours
if A >= 24:
    A = A - 24
B = minutes

print("%d %d" % (A, B))
