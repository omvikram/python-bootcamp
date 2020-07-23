## SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    if(0 in nums and 7 in nums):
        print(nums)
        index_of_first_zero = nums.index(0)
        index_of_second_zero = nums.index(0, index_of_first_zero+1, len(nums))
        index_of_seven = nums.index(7)
        print(str(index_of_first_zero) + " " + str(index_of_second_zero) + " " + str(index_of_seven))
        if(index_of_first_zero < index_of_second_zero < index_of_seven):
            return True
        else:
            return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

## COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(num):
    prime_list = []
    divisible = False
    for i in range(2,num):
        for j in range(2,i):
            if(i%j==0):
                divisible = True
                break
            else:
                divisible = False
                pass
        if (not divisible):
            prime_list.append(i)

    return prime_list
print(count_primes(10))


