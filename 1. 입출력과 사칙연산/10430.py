#첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

A, B, C = map(int, input().split())

print("%d" % ((A + B) % C))
print("%d" % (((A % C) + (B % C)) % C))
print("%d" % ((A * B) % C))
print("%d" % (((A % C) * (B % C)) % C))