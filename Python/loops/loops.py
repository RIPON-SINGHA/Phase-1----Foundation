# here i am learnign about the concept of "loop" in python.
# loops can perform operations multiple times as user commanded to do.
# the codes that needs to be execute multiple times will execute in a loop.

#there is two types of loops in python 1> while loop and 2> for loop

# while loop:
# printing my name multiple times.
i = 1
while(i <= 5):
    print("Ripon")
    i = i + 1 # another way to increment "i" is using "+=" operator


i = 0
while(i < 5):
    print("Meow")
    i += 1



# for loop:
# print my name multiple times.
for i in [0, 1, 2]: # we are using list in term of iterating. in lython list is a datatype that can store multiple values of different other data types.
    print("Ripon")


# we can also do it like this>
for i in range(3): # we are using built in function "range()" to specify the iteration count.
    print("Bark")


# we can also do this if we dont need that "i" for further operation
for _ in range(3):
    print("vs code")
# "_" is used for just to iterate through the range if the variable of iteration is not needed in further use like "i" does not being used anywhere.



# another way to do multiple execution of some specific code we can use this:
print("Avengers Assamble\n" * 3, end = "") 
# using this statement we can performe same logic multiple times and by using end="" we can destroy the next line entered by the print function.




# using both loops for printing a statement multiple times based on user input.
# validating user input using while loop so it cant be zero and less than zero.
while True: # while True means it is always true and when "n" is positive "break" will exit the if and loop at once.
    n = int(input("what's n? "))
    if(n > 0):
        break


# printing the statement based on positive user input using for loop.
for _ in range(n):
    print("I am learning python!")



# creating the same code logic with functions
def main():
    meow(5)


def meow(n):
    while True:
        n = int(input("what's n? "))
        if(n>0):
            break
    
    for _ in range(n):
        print("meow!")

main()


# creating the same logic with three functions.
# defining main() function for main operation
def main():
    number = get_number()
    meow(number)

# creating a function for validation the user input whether its positive or negative
def get_number():
    while True:
        n = int(input("what's n? "))
        if(n > 0):
            return n
        
# creating a function that will print the statement n times that is based on the function call parameter ( which will be given by get_number() function )
def meow(n):
    for _ in range(n):
        print("MEOW")

# callign the main() function
main()


