# defining fucntion : user define function 
def hello(): #using "def" keyword we can define function in python
    print("hello World!")

hello() # function call. calling a function will execute the function and its inside program





# user define functions can take arguments and can use those arguments as parameters in function calling.
def hii(name):
    print(f"hello {name}")

# here 'Name' is the parameter for this function calling which directs to the arguments of hii() function's argument 'name'
# arguments and parametes can have different name
Name = input("What is your name: ")
hii(Name)





# we can set a function's arguments default for default parameter such as no parameter
def sayHello(to = "world"):
    print(f"Hello {to}")

sayHello()
# we can also change the default argument value in function calling using a user parameter
naam = input("enter you name: ")
sayHello(naam)
# default argument and parameter will work in both ways whether a parameter is given in calling or not.



# we can use function inside another like this.
def main():
    name = input("Enter your name: ")
    hi(name) # we are using hi() function inside the main() function


def hi(name):
    print("Hello", name)


main() # and calling the main() function to execute both the main() and hi() function together
# main() is asking for a input then executing the hi() fucntion which will print the "hello + name" statement.