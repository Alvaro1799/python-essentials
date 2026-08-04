# TYPE CASTING - PE1 Module 2
# Convertir un tipo de dato a otro

# int() convierte a entero
print(int("17")) #string a int
print(int(1.79)) #float a int (no redondea, solo quita los decimales)

#float() convierte a decimal
print(float("3.14")) #string a float
print(float(5)) #int a float

#str() convierte a string
print(str(123)) #int a string
print(str(3.14)) #float a string

#bool() convierte a booleano
print(bool(1)) # True
print(bool(0)) # False
print(bool("")) # False - string vacio
print(bool("Hola")) # True - string no vacio
print(bool([])) # False - lista vacia
print(bool([1, 2, 3])) # True - lista no vacia
