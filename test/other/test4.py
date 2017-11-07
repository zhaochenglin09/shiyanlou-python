import math

x = float(input("Enter an number: "))

n = temp3 = temp4= 1

temp2 = 0

for n in range (1, 100):

    temp3 *= n

    temp2 = math.pow(x, n)

    temp4 += temp2 / temp3
    
    if temp2/temp3 < 0.0001:
        break

print("n is {} cale is {:.10f}".format(n,temp4))
