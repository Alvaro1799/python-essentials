i = 15
j = 22

#& (ampersand) ‒ bitwise conjunction;
#| (bar) ‒ bitwise disjunction;
#~ (tilde) ‒ bitwise negation;
#^ (caret) ‒ bitwise exclusive or (xor).

log = i and j
#We are dealing with a logical conjunction here. 
#Let's trace the course of the calculations. 
#Both variables i and j are not zeros, so will be deemed to represent True. 
#Consulting the truth table for the and operator, we can see that the result will be True. 
#No other operations are performed.

#Now the bitwise operation 
bit = i & j
#The & operator will operate with each pair of corresponding bits separately, 
#producing the values of the relevant bits of the result.

#Let's look at the negation operators 
logneg = not i
#The logneg variable will be set to False ‒ nothing more needs to be done.

#The bitwise negation goes like this
bitneg = ~i
#It may be a bit surprising: the bitneg variable value is -16. 
#This may seem strange, but isn't at all. If you wish to learn more, 
#you should check out the binary numeral system and the rules governing two's complement numbers.

#Each of these two-argument operators can be used in abbreviated form. 
#These are the examples of their equivalent notations:

#x = x & y OR  x &= y
#x = x | y OR  x |= y
#x = x ^ y OR  x ^= y

#How do we deal with single bits?
#flag_register = 0000000000000000000000000000x000

#Check the state of your bit ‒ you want to find out the value of your bit; 
#comparing the whole variable to zero will not do anything, 
#because the remaining bits can have completely unpredictable values,
#but you can use the following conjunction property:
x & 1 = x
x & 0 = 0

#If you apply the & operation to the flag_register variable along with the following bit image:
#00000000000000000000000000001000

#Let's build a bit mask to detect the state of your bit. 
#It should point to the third bit. That bit has the weight of 23 = 8. 
#A suitable mask could be created by the following declaration:
the_mask = 8
#You can also make a sequence of instructions depending on the state of your bit. 
if flag_register & the_mask:
    #My bit is set
else:
    #My bit is reset

#Reset your bit ‒ you assign a zero to the bit while all the other bits must remain unchanged; 
#let's use the same property of the conjunction as before, 
#but let's use a slightly different mask ‒ exactly as below:
11111111111111111111111111110111

#Note that the mask was created as a result of the negation of all the bits 
#of the_mask variable. Resetting the bit is simple, and looks like this 
flag_register &= ~the_mask 

#Set your bit ‒ you assign a 1 to your bit, while all the remaining bits 
#must remain unchanged; use the following disjunction property:
x | 1 = 1
x | 0 = x

#You're now ready to set your bit with one of the following instructions
flag_register |= the_mask 

#Negate your bit ‒ you replace a 1 with a 0 and a 0 with a 1. 
#You can use an interesting property of the xor operator
x ^ 1 = ~x
x ^ 0 = x

#and negate your bit with the following instructions
flag_register ^= the_mask 

#shifting
#The shift operators in Python are a pair of digraphs: << and >>, clearly suggesting in which direction the shift will act.

#value << bits
#value >> bits 

var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

#17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1) → 8 
#(shifting to the right by one bit is the same as integer division by two)

#17 << 2 → 17 * 4 (17 multiplied by 2 to the power of 2) → 68 
#(shifting to the left by two bits is the same as integer multiplication by four)

#Python supports the following logical operators:

#    and → if both operands are true, the condition is true, e.g., (True and True) is True,
#    or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
#    not → returns false if the result is true, and returns true if the result is false, e.g., not True is False.

#2. You can use bitwise operators to manipulate single bits of data. The following sample data:

#    x = 15, which is 0000 1111 in binary,
#    y = 16, which is 0001 0000 in binary.

#will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:

#    & does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
#    | does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
#    ˜ does a bitwise not, e.g., ˜ x = 240*, which is 1111 0000 in binary,
#    ^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
#    >> does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
#    << does a bitwise left shift, e.g., y << 3 = 128, which is 1000 0000 in binary.

#* -16 (decimal from signed 2's complement) -- read more about the Two's complement operation.