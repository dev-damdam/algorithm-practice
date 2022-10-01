S = input()

start = ord("a")
end = ord("z")

for i in range(start, end + 1):
    print(S.find(chr(i)), end=" ")
