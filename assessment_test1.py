## Statements Assessment Test 1
## https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/

#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = "Print only the words that start with s in this sentence"
ls = st.split(" ")
for words in ls:
    if(words.startswith('s')):
        print(words)

# # #Use range() to print all the even numbers from 0 to 10.
for i in range(11):
    if(i%2 == 0):
        print(i)

# # #Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
for i in range(1,50):
    if(i%3 == 0):
        print(i)

# #Go through the string below and if the length of a word is even print "even!"
steven = 'Print every word in this sentence that has an even number of letters'
lseven = steven.split(" ")
for wordeven in lseven:
    if(len(wordeven)/2 == 0):
        print(wordeven)
    else:
        print("ha ha there is None")

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for num in range(1,100):
    if(num%3==0 and num%5==0):
        print("Fizzbuzz")
    elif(num%3==0):
        print("Fizz")
    elif(num%5==0):
        print("Buzz")

#Use List Comprehension to create a list of the first letters of every word in the string below:
stfirst = 'Create a list of the first letters of every word in this string'
lsfirst = stfirst.split(" ")
result = []
for each in lsfirst:
    result.append(each[0:1])
    print(result)
