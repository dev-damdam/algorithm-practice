#ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
count = 0
for i in alpha:
    count += word.count(i)
print(len(word) - count)