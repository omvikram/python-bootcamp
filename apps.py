##bootcamp file for practice
inputStr = "Python for Beginners"

print(inputStr.find("for")) ## will tell you the first index of 'for'
print(inputStr.replace("for", "4")) ##will replace for by 4 in the inputStr

myList = [2,4,6,8,10]

print(myList[0])
print(myList[-1])
print(myList[0:3])
print(6 in myList)
myList.insert(0,-1)
print(myList)

newList = range(0,10)
for number in newList:
    print(number)