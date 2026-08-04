numbers = [10, 5, 7, 2, 1] 
#list are always numbered starting from zero
#our list is a collection of elements, but each element is a scalar.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("\nNew list contents:", numbers)  # Printing current list contents. 
#The value inside the brackets which selects one element of the list is called an index, 
#while the operation of selecting an element from the list is known as indexing.

#Note: all the indices used so far are literals. Their values are fixed at runtime, 
#but any expression can be the index, too. This opens up lots of possibilities.
print(numbers[0]) # Accessing the list's first element.
#The function takes the list's name as an argument, 
#and returns the number of elements currently stored inside the list 
print("\nList length:", len(numbers))  # Printing the list's length.
print(numbers) # Printing the whole list.

#Any of the list's elements may be removed at any time ‒ 
#this is done with an instruction named del (delete). Note: it's an instruction, not a function.
#You have to point to the element to be removed ‒ 
#it'll vanish from the list, and the list's length will be reduced by one.
del numbers[1]
print(len(numbers))
print(numbers)

#You can't access an element which doesn't exist ‒ 
#you can neither get its value nor assign it a value
#print(numbers[4])
#numbers[4] = 1

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList's length:", len(numbers))  # Printing previous list length.

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

#It may look strange, but negative indices are legal, and can be very useful.
#An element with an index equal to -1 is the last one in the list

print(numbers[-1])
