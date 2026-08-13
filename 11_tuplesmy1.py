'''The first and the clearest distinction between lists and 
tuples is the syntax used to create them - tuples prefer to use parenthesis, 
whereas lists like to see brackets, although it's also possible to create a 
tuple just from a set of values separated by commas.'''

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

'''One of the most useful tuple properties is their ability to appear 
on the left side of the assignment operator. You saw this phenomenon some time ago, 
when it was necessary to find an elegant tool to swap two variables' values.'''

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

'''It shows three tuples interacting − in effect, 
the values stored in them "circulate" − t1 becomes t2, t2 becomes t3, and t3 becomes t1.

Note: the example presents one more important fact: 
a tuple's elements can be variables, not only literals. Moreover, 
they can be expressions if they're on the right side of the assignment operator.'''

