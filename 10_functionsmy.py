def valuees():
    print("Enter a value: ")

valuees()
a = int(input())
valuees()
b = int(input())
valuees()
c = int(input())

'''
1. A function is a block of code that performs a specific task when the function is 
called (invoked). You can use functions to make your code reusable, better organized, 
and more readable. Functions can have parameters and return values.
'''

'''2. There are at least four basic types of functions in Python:

built-in functions 
pre-installed modules 
user-defined functions 
lambda functions
'''

'''3. You can define your own function using the def keyword and the following syntax:
'''

def your_function(optional parameters):
    # the body of the function 


#You can define a function which doesn't take any arguments, e.g.

def message():    # defining a function
    print("Hello")    # body of the function

message()    # calling the function

'''You can define a function which takes arguments, too, just like the one-parameter function below:'''

def hello(name):    # defining a function
    print("Hello,", name)    # body of the function


name = input("Enter your name: ")

hello(name)    # calling the function

'''A parameter is actually a variable, but there are two important factors that 
make parameters different and special:

    parameters exist only inside functions in which they have been defined, 
    and the only place where the parameter can be defined is a space between a 
    pair of parentheses in the def statement;
    assigning a value to the parameter is done at the time of the function's 
    invocation, by specifying the corresponding argument.
'''

'''Don't forget:

    parameters live inside functions (this is their natural environment)
    arguments exist outside functions, and are carriers of values passed 
    to corresponding parameters.
'''

def message(number):
    print("Enter a number:", number)

'''A value for the parameter will arrive from the function's environment.

Remember: specifying one or more parameters in a function's definition is 
also a requirement, and you have to fulfil it during invocation. You must provide as many 
arguments as there are defined parameters.

Failure to do so will cause an error.'''