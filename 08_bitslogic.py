# LOGIC AND BIT OPERATIONS - PE1 Module 3.3

# Operadores lógicos
print(True and True)    # True
print(True and False)   # False
print(True or False)    # True
print(False or False)   # False
print(not True)         # False

# Combinados
x = 5
print(x > 3 and x < 10)   # True
print(x < 3 or x > 10)    # False

# Bitwise operators (operan sobre bits)
print(5 & 3)    # AND  → 1
print(5 | 3)    # OR   → 7
print(5 ^ 3)    # XOR  → 6
print(~5)       # NOT  → -6
print(5 << 1)   # shift left  → 10
print(5 >> 1)   # shift right → 2