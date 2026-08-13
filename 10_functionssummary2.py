#4.3.9 SECTION SUMMARY

#1. You can use the return keyword to tell a function to return some value. The return statement exits the function, e.g.:

def multiply(a, b):
    return a * b
 
print(multiply(3, 4)) # outputs: 12
 
 
def multiply(a, b):
    return
 
print(multiply(3, 4)) # outputs: None
 

#2. The result of a function can be easily assigned to a variable, e.g.:

def wishes():
    return "Happy Birthday!"
 
w = wishes()
 
print(w) # outputs: Happy Birthday!
 

#Look at the difference in output in the following two examples:

# Example 1
def wishes():
    print("My Wishes")
    return "Happy Birthday"
 
wishes() # outputs: My Wishes
 
 
# Example 2
def wishes():
    print("My Wishes")
    return "Happy Birthday"
 
print(wishes())
 
# outputs: My Wishes
# Happy Birthday
 

#3. You can use a list as a function's argument, e.g.:

def hi_everybody(my_list):
    for name in my_list:
        print("Hi,", name)
 
hi_everybody(["Adam", "John", "Lucy"])
 

#4. A list can be a function result, too, e.g.:

def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list
 
print(create_list(5))
 
