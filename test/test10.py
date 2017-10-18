a = [[0]*10]*10

print("-"*50)

for i in range (1, 11):

    for j in range(1, 11):

        a[i-1][j-1] = i * j
        
        print("{:4d}".format(a[i-1][j-1]), end=' ')



    print()

print("-"*50)
