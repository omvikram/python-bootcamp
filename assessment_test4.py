## Write a function that computes the volume of a sphere given its radius.

def volume_of_sphere(radius):
    pi = 3.14157
    volume = (4*pi*(radius**3))/3
    return volume

print(volume_of_sphere(2))

## Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    mylist = []
    for each in range(low, high):
        mylist.append(each)
        
    if(num in mylist):
        return True
    else:
        return False

print(ran_check(5,2,7))


## Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(mystring):
    count_low = 0
    count_high = 0
    for ch in mystring:
        if(ord(ch) >= 65 and ord(ch) < 90):
            count_high = count_high+1
        elif(ord(ch) >= 97 and ord(ch) < 123):
            count_low = count_low+1
    return count_low, count_high

print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

## Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    mylist = []
    for item in lst:
        if(item not in mylist):
            mylist.append(item)
    
    return mylist

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

## Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    return(lambda numbers : numbers * numbers)

print(multiply([1,2,3,-4]))

## Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(inputstr):
    abc = []
    for ch in inputstr:
        abc.append(ch)
    abc.reverse()
    revstr = "".join(abc)

    if(revstr == inputstr):
        return True
    else:
        return False


print(palindrome('helleh'))
print(palindrome('dalda'))
print(palindrome('malayalam'))


## Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
def is_pangram(str1):
    str1 = str1.replace(" ", "")
    str1 = str1.lower()
    small = []
    xsmall =[]
    for num in range(97,123):
        small.append(num)
        xsmall.append(num)
    
    templist = []
    for ch in str1:
        if(ord(ch) in small):
            small.remove(ord(ch))
        else:
            templist.append(ord(ch))

    print(small)
    if(len(small)==0):
        if(len(templist) > 0):
            for each in templist:
                if(each in xsmall):
                    return True
                else:
                    return False
        return True
    else:
        return False

print(is_pangram("The quick brown fox jumps over the lazy dog"))


