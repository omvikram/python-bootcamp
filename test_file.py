myfile = open("test.txt")
print(myfile.read())

myfile.seek(0)
print(myfile.read())

myfile.seek(0)
print(myfile.readlines())

myfile.close()

############################################

with open("test.txt", mode="a") as f1:
    f1.write("Om is writing...")

with open("test.txt", mode="r") as f2:
    print(f2.read())

with open("test.txt", mode="w") as f3:
    f3.write("THIS IS NEW FILE")

with open("test.txt", mode="r") as ffs:
    print(ffs.read())