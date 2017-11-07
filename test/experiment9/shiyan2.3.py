
name = input("Enter file name: ")

fobj = open(name)

print(fobj.read())

fobj.close()
