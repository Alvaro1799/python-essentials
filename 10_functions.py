# FUNCTIONS - PE1 Module 4

# Función básica
def greet():
    print("Hola!")

greet()

# Con parámetros
def greet_user(name):
    print("Hola, " + name + "!")

greet_user("Alvaro")

# Con return
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# Múltiples parámetros con default value
def power(base, exp=2):
    return base ** exp

print(power(3))     # 9 - usa default
print(power(3, 3))  # 27

# Return múltiple
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max([4, 1, 7, 2])
print(lo, hi)  # 1 7

# Scope - variable local vs global
x = 10  # global

def my_func():
    x = 20  # local - no afecta la global
    print(x)

my_func()   # 20
print(x)    # 10 - sigue siendo 10

# None - función sin return devuelve None
def no_return():
    pass

print(no_return())  # None