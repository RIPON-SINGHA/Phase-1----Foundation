# this is to understand python conditons with conditional operators
# conditions are asked questions to python in based of its answer (true and false) we can perform operations

# the conditional operators are : <, <=, >, >=, ==, !=

# conditions can be define by using some key words in python
# "if" keyword
x = int(input("what's x? "))
y = int(input("what's y? "))

if(x > y):
    print("x is greater than y")

if(x < y):
    print("x is lesser than y")

if(x == y):
    print("x is equal to y")
# usig too much if can cause readability of code to difficult so we use another keyword to perform same condition and operation without using multiple ifs


#using "elif" we can achieve the less if redundancy in code and better code readability
n1 = int(input("what's n1? "))
n2 = int(input("what's n2? "))

if(n1 < n2):
    print("n1 is lesser than n2")
elif(n1 > n2):
    print("n1 is greater than n2")
elif(n1 == n2):
    print("n1 is equal to n2")



# we can achieve more non redundancy by using "else" keyword at the last of the conditions. using "else" code will execute the default operation if no condition is true.
num1 = int(input("what's num1? "))
num2 = int(input("what's num2? "))

if(num1 > num2):
    print("num1 is greater than num2")
elif(num1 < num2):
    print("num1 is lesser than num2")
else:
    print("num1 is equal to num2")


#using the operator !=
number1 = int(input("what's number1? "))
number2 = int(input("what's number2? "))

if(number1 != number2):
    print("number1 is not equal to number 2")
else:
    print("number1 is equal to number2")


# another version of that code
if(number1 == number2):
    print("number1 and number2 are equal")
else:
    print("number1 and number2 is not equal at all")