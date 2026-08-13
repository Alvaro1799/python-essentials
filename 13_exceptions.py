# EXCEPTIONS - PE1 Module 4
# Manejo de errores para que el programa no crashee

# Try / except básico
try:
    result = 10 / 0
except ZeroDivisionError:
    print("No puedes dividir entre cero!")

# Capturar el error como variable
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)

# Múltiples excepciones
try:
    number = int(input("Dame un número: "))
    result = 10 / number
    print(result)
except ValueError:
    print("Eso no es un número!")
except ZeroDivisionError:
    print("No puedes usar cero!")

# Except genérico - atrapa cualquier error
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except Exception as e:
    print("Algo salió mal:", e)

# Finally - corre siempre, haya error o no
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
finally:
    print("Esto siempre se ejecuta")

# Else - corre solo si NO hubo error
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print("Todo bien, resultado:", result)

# Excepciones comunes en Python
# ValueError      → tipo incorrecto (int("abc"))
# ZeroDivisionError → dividir entre 0
# IndexError      → index fuera de rango
# KeyError        → key no existe en dict
# TypeError       → operación en tipo incorrecto
# FileNotFoundError → archivo no encontrado