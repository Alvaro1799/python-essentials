'''It's legal, and possible, to have a variable named the same as a function's parameter.'''

'''def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)
'''

'''def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")
'''

'''def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")
'''

'''keyword argument passing.'''

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

'''
You can mix both styles if you want ‒ there is only one unbreakable rule: 
you have to put positional arguments before keyword arguments.

If you think for a moment, you'll certainly guess why.

To show you how it works, we'll use the following simple three-parameter function:'''

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1,2,3)

'''Of course, you can replace such an invocation with a purely keyword variant, like this:'''

adding(c = 1, a = 2, b = 3)

'''Let's try to mix both styles now.

Look at the function invocation below:'''

adding(3, c = 1, b = 2)

'''Let's analyze it:

    the argument (3) for the a parameter is passed using the positional way;
    the arguments for c and b are specified as keyword ones.'''

'''Parametrized functions – more details'''
def introduction(first_name, last_name="Smith"):
     print("Hello, my name is", first_name, last_name)

introduction("James", "Doe")

introduction(first_name="William")

