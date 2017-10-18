a = [[0 for x in range(10)] for y in range(10)]

b =[[0]*10]*10

for i in range(10):

    for j in range(10):

        b[2][0]= 2        

        print("a[{}][{}]={}".format(i, j, a[i][j]),end=' ')

    print()

print("-"*50)

for i in range(10):

    for j in range(10):

        b[2][0]= 2 

        print("b[{}][{}]={}".format(i, j, b[i][j]),end=' ')

    print()
print("-"*50)

print(a==b)


