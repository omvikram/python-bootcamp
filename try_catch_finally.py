## Handle the exception thrown by the code below by using try and except blocks.
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("Please enter a valid number")
finally:
    print("This block will execute always")


# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

x = 5
y = 0

try:
    z = x/y
except:
    print("Do not divide by zero or less number")
finally:
    print("All Done")

# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def square():
    while True:
        result = 0
        try:
            abc = input("Please enter a number")
            result = abc**2
        except:
            print("Please enter a valid number")
            continue
        else:
            if(result > 0):
                print(result)
                break
if __name__ == "__main__":
    square()