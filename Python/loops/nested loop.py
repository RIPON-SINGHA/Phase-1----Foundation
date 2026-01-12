# nested loop is a loop in another loop.
# the first loop is called outer loop and the loop inside it called inner loop and middle loop if there is 3 loop in total
# nested loop is used to handle the logics that requires repeatative actions within another repeatative actions.

# printing a square with nested loop.

for i in range (5):   # defines each row in the square
    for j in range (5):   # defines each "*" in the square 
        print("*", end="")   # printing the "*"
    print()   # adding a new line after one row is coompleted


# we can also do that logic without using nested loop:
for i in range(5):
    print("*" * 5)




# using functions:
def main():  # main() function for conducting the main action
    print_square(5)


def print_square(size):  # print_square() function is for printing the square based on the parameter in function call
    for i in range(size):
        for j in range(size):
            print("*", end="")
        print()

main()  # calling the main() function






# using multiple function to break the process into different function
# main function doing its work to perform the main action
def main():
    print_square(5)

# print_square() function printing the square by a loop by calling the print_rows() function
def print_square(size):
    for _ in range(size):
        print_rows(size)

# print_rows() function printing rows 
def print_rows(width):
    print("*" * width)

# calling the main() function
main()

# breaking a program generally a larger program into small components as functions is a good habit to better understanding and readability



# CREATING DIFFERENT TYPES OF ANGLE PATTERNS USING NESTED LOOPS

# Right angled pattern
for i in range(1, 6):            # *
    for j in range(i):           # **
        print("*",end="")        # ***
    print()                      # ****
                                 # *****



# Up side down right angled pattern
for i in range(5, 0, -1):        # *****
    for j in range(i):           # ****
        print("*", end="")       # ***
    print()                      # ** 
                                 # *



# Left angled pattern
for i in range(1, 6):            #     *
    for j in range(5, i, -1):    #    **
        print(" ", end="")       #   ***
    for k in range(i):           #  ****
        print("*", end="")       # *****
    print()



#Up side down left angled pattern
for i in range(1, 6):            # *****
    for j in range(6, i, -1):    #  ****
        print("*", end= "")      #   ***
    print()                      #    **
                                 #     *
    for k in range(i):          
        print(" ", end="")
