
n = int(input("Enter the number of students: "))

Subjects = ['Maths', 'Physics', 'History']

data = {}

for x in range(0, n):

    name = input("Enter the name of student {} :".format(x + 1))

    for i in Subjects:

        data.setdefault(name, [] ).append(int(input("Enter {}'s mark of {} :".format(name, i))))

print (data)

print (data.values())
for x, y in data.items():

    total = sum(y)

    print("{}'s total mark is {} ".format(x, total))

    if total < 120:
        print("failed ")

    else:
        print("passed ")
