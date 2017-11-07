amount = float(input("Enter amount: "))

inrate = float(input("Enter Inrate rate: "))

period = float(input("Enter period: "))

value = 0

year = 1

while year <= period:

    value = amount + (inrate * amount)

    print("Year {} Sum {:.2f}".format(year,value))

    amount = value

    year = year + 1
