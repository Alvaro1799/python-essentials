'''The dictionary is another Python data structure. 
It's not a sequence type (but can be easily adapted to 
sequence processing) and it is mutable.

To explain what the Python dictionary actually is, 
it is important to understand that it is literally a dictionary.'''

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

'''This means that a dictionary is a set of key-value pairs. Note:

    each key must be unique − it's not possible to have more than one key of the same value;
    a key may be any immutable type of object: it can be a number (integer or float), 
    or even a string, but not a list;
    a dictionary is not a list − a list contains a set of numbered values, while a 
    dictionary holds pairs of values;
    the len() function works for dictionaries, too − it returns the number of 
    key-value elements in the dictionary;
    a dictionary is a one-way tool − if you have an English-French dictionary, 
    you can look for French equivalents of English terms, but not vice versa. '''

print(dictionary['cat'])
print(phone_numbers['Suzy'])


'''Note:

    if the key is a string, you have to specify it as a string;
    keys are case-sensitive: 'Suzy' is something different from 'suzy'.
'''

'''When you write a big or lengthy expression, 
it may be a good idea to keep it vertically aligned. 
This is how you can make your code more readable and more programmer-friendly, e.g.:'''

# Example 1:
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
}
# Example 2:
phone_numbers = {'boss': 5551234567,
              'Suzy': 22657854310
}

#This kind of formatting is called a hanging indent.

'''method named keys(), possessed by each dictionary. The method returns an 
iterable object consisting of all the keys gathered within the dictionary. 
Having a group of keys enables you to access the whole dictionary in an easy and handy way.'''

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

'''Let's now have a look at a dictionary method called items(). 
The method returns tuples (this is the first example where tuples are something more 
than just an example of themselves) where each tuple is a key-value pair.'''

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)

'''Modifying and adding values

Assigning a new value to an existing key is simple - 
as dictionaries are fully mutable, there are no obstacles to modifying them.

We're going to replace the value "chat" with "minou", 
which is not very accurate, but it will work well with our example.'''

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)

#Do you want it sorted? Just enrich the for loop to get such a form:

for key in sorted(dictionary.keys()):

#ere is also a method called values(), which works similarly to keys(), but returns values.

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in dictionary.values():
    print(french)

'''Adding a new key

Adding a new key-value pair to a dictionary is as simple as changing a value – 
you only have to assign a value to a new, previously non-existent key.

Note: this is very different behavior compared to lists, which don't allow you 
to assign values to non-existing indices.

Let's add a new pair of words to the dictionary − a bit weird, but still valid:'''

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne'
print(dictionary)

#You can also insert an item to a dictionary by using the update() method, e.g.:

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.update({"duck": "canard"})
print(dictionary)

#Removing a key

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

del dictionary['dog']
print(dictionary)

#Note: removing a non-existing key causes an error.

#To remove the last item in a dictionary, you can use the popitem() method:

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.popitem()
print(dictionary)    # outputs: {'cat': 'chat', 'dog': 'chien'}

#In the older versions of Python, i.e., before 3.6.7, 
# the popitem() method removes a random item from a dictionary.

#showing how tuples and dictionaries can work together.

school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
