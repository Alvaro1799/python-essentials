# OPERATORS - PE1 Module 2
# Los operadores manipulan valores y variables

# Aritméticos
print (10 + 7) #suma
print (10 - 7) #resta
print (10 * 7) #multiplicación
print (10 / 7) #división (Siempre float)
print (10 // 7) #división entera
print (10 % 7) #módulo (resto de la división)
print (10 ** 2) #potencia

# Comparación (Devuelven True o False)
print (10 > 7)  # mayor que
print (10 < 7)  # menor que
print (10 == 7) # igual a
print (10 != 7) # diferente de
print (10 >= 7) # mayor o igual que
print (10 <= 7) # menor o igual que

#prioridad de operadores
print (10 + 5 * 2) # multiplicación primero, luego suma
print ((10 + 5) * 2) # parentesis primero, luego multiplicación

# operador "in" verifica si algo esta dentro de
print("a" in "Alvaro") #True
print("z" in "Alvaro") #False
print(5 in (1,2,3,4,5)) #True

#operador "not in"
print("z" not in "Alvaro") #True