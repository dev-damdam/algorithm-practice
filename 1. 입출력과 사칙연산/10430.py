#첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

A, B, C = input().split()

print("%d" % ((int(A) + int(B)) % int(C)))
print("%d" % (((int(A) % int(C)) + (int(B) % int(C))) % int(C)))
print("%d" % (int(A) * int(B) % int(C)))
print("%d" % (((int(A) % int(C)) * (int(B) % int(C))) % int(C)))