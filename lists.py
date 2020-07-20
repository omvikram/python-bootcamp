vowels = ["a", "e", "i", "o", "u"]
word = "One Missisipi"
newword = "Don't panic"
newlist = []

for ch in word:
    eachStr = str(ch)
    if eachStr in vowels:
        print("its already present")
    else:
        vowels.append(eachStr)
         print(vowels)

##ist functionalities
for ch in newword:
    eachStr = str(ch)
    newlist.append(eachStr)

print(newlist)
newlist.remove("D")
newlist.remove("a")
newlist.remove("i")
newlist.remove("c")

newlist.pop(2)
newlist.pop(3)
newlist.pop(4)

newlist.insert(2," ")
newlist.insert(4,"o")
print(newlist)
