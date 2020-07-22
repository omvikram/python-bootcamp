#using print statement in function
def my_first_function(name='Default'):
    print("Hello : " + name)

my_first_function("Om")
my_first_function()

#using return statement in function
def sum_of_numbers(num1, num2):
    return num1+num2

result = sum_of_numbers(2,3)
print(result)

#using return and print in function
evenlist = []
def is_even_number(testlist):
    for num in testlist:
        if(num%2 == 0):
            evenlist.append(num)
    return evenlist

resultlist = is_even_number([1,2,3,4,5,6,7,8,9])
print(resultlist)

#using tuples as return in function
def compare_salary(list_tuple):
    curr_salary = 0
    curr_employee = ''
    for employee,salary in list_tuple:
        if(salary > curr_salary):
            curr_salary = salary
            curr_employee = employee
        else:
            pass
    return (curr_employee, curr_salary)

result_tuple = compare_salary([('A',100),('B',500), ('C', 300), ('D', 200)])
print(result_tuple)

#function skyLine - even UPPERCASE, odd lowercase
def myfunc(testStr):
    mylist = []
    for index in range(0, len(testStr)):
        if(index%2==0):
            mylist.append(testStr[index].upper())
        else:
            mylist.append(testStr[index].lower())
    return ConvertToString(mylist)

def ConvertToString(liststr):
    resultStr =''
    return resultStr.join(liststr)  


print(myfunc("Mississipi"))