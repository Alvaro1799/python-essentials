# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

### Second way

# Read two numbers
#number1 = int(input("Enter the first number: "))
#number2 = int(input("Enter the second number: "))

# Choose the larger number

#if number1 > number2: larger_number = number1 (if any of the if-elif-else branches contains 
#just one instruction, you may code it in a more comprehensive form 
#(you don't need to make an indented line after the keyword, 
#but just continue the line after the colon).)
#Keep this in mind to read someone else's code and understand it better,

#else: larger_number = number2

# Print the result
#print("The larger number is:", larger_number)

