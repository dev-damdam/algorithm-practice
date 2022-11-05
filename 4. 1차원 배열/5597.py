submit_students = []
temp = []

for i in range(0, 30):
    temp.append(i + 1)

for i in range(0, 28):
    submit_students.append(int(input()))

not_submit_students = list(set(temp).difference(set(submit_students)))
not_submit_students.sort()

for not_submit in not_submit_students:
    print(not_submit)
