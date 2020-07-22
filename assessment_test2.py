##https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

## LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens(num1,num2):
    if(num1%2==0 and num2%2==0):
        if(num1 > num2):
            return num2
        else:
            return num1
    else:
        if(num1 > num2):
            return num1
        else:
            return num2

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(3,5))


## ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    mylist = text.split(" ")
    if(mylist[0][0:1] == mylist[1][0:1]):
        return True
    else:
        return False

print(animal_crackers("Hasta Hirshima"))
print(animal_crackers("Nagashaki Hirshima"))


## MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(n1,n2):
    if(n1 == 20 or n2 == 20):
        return True
    elif((n1+n2) == 20):
        return True
    else:
        return False

print(makes_twenty(20,10))
print(makes_twenty(10,10))
print(makes_twenty(2,3))

## OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    resultStr = ""
    mylist = []
    for index in range(0, len(name)):
        if(index == 0 or index == 3):
            mylist.append(name[index].upper())
        else:
            mylist.append(name[index])
    return resultStr.join(mylist)

print(old_macdonald("macdonald"))

## MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(stmt):
    resultStr = ""
    newlist = stmt.split(" ")
    revlist = []
    for each in newlist:
        revlist.append(each)
    revlist.reverse()
    return revlist
    #return resultStr.join(revlist)

print(master_yoda("Here am I"))

## ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(number):
    if((number > 89 and number < 111) or (number > 189 and number < 211)):
        return True
    else:
        return False

print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

## Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(numslist):
    for i in range(0, len(numslist)):
        if(i+1 < len(numslist)):
            if(numslist[i] == 3 and numslist[i+1] == 3):
                return True
            else:
                pass
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

## PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    newStr = ""
    for each in text:
        newStr = newStr + str(each*3)
    print(newStr)

paper_doll('Hello')
paper_doll('Mississippi')

## BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
## If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    sum = a+b+c
    if(sum <= 21):
        return sum
    elif(sum > 11 and (a ==11 or b == 11 or c == 11)):
        return sum - 10
    else:
        return "BUST"

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

## SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 
## (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    sum = 0
    index_of_6 = arr.index(6)
    index_of_9 = arr.index(9)

    if(index_of_6 > 0 and index_of_9 > 0):
        if(index_of_6 < index_of_9):
            for i in range(0, len(arr)):
                if(i >= index_of_6 and i <= index_of_9):
                        pass
                else:
                    sum = sum + arr[i]
        else:
            for i in range(0, len(arr)):
                sum = sum + arr[i]
            return sum
    else:
        for i in range(0, len(arr)):
            sum = sum + arr[i]
        return sum

#print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

        

