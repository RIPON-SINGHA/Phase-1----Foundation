# here we will check whether a number is odd or even by using if elid and function

#using if and elif
num = int(input("what's your numebr? "))

if(num % 2 == 0):
    print(f"your number {num} is Even")
else:
    print(f"Your number {num} is Odd")



#using function because it helps us to use same line code multiple times without writing it
def main():
    number = int(input("what's your number? "))

    if isEven(number):
        print(f"Your number {number} is Even")
    else:
        print(f"Your number {number} is Odd")


def isEven(num):

    if(num % 2 == 0):
        return True
    else:
        return False



# we can use pythonic expression for operations like if and else with just two result true or false
# as we defined a function isEven() for checking a number is even or odd, we can do much simpler than we did earlier

def isEven(num):
    return True if(num % 2 == 0) else False



main() # calling the main( function