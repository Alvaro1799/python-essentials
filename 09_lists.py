# LISTS - PE1 Module 3
# Colección ordenada y mutable de elementos

# Crear una lista
my_list = [1, 2, 3, 4, 5]
mixed = ["Alvaro", 27, True, 3.14]
empty = []

# Indexing
print(my_list[0])    # 1 - primer elemento
print(my_list[-1])   # 5 - último elemento

# Slicing
print(my_list[1:3])  # [2, 3] - end no se incluye
print(my_list[:3])   # [1, 2, 3] - desde el inicio
print(my_list[2:])   # [3, 4, 5] - hasta el final
print(my_list[:])    # copia toda la lista

# Modificar
my_list[0] = 10
print(my_list)       # [10, 2, 3, 4, 5]

# Métodos útiles
my_list.append(6)        # agrega al final
my_list.insert(0, 99)    # inserta en index 0
del my_list[0]           # elimina por index
my_list.remove(6)        # elimina por valor

# Funciones built-in
print(len(my_list))      # cantidad de elementos
print(min(my_list))      # valor mínimo
print(max(my_list))      # valor máximo
print(sum(my_list))      # suma total

# Ordenar
my_list.sort()           # ordena la lista original
my_list.sort(reverse=True)  # ordena descendente
my_list.reverse()        # invierte el orden

# Iterar
for item in my_list:
    print(item)

# in operator con listas
print(3 in my_list)      # True o False

# CUIDADO - esto NO es una copia
list_a = [1, 2, 3]
list_b = list_a          # misma lista en memoria
list_c = list_a[:]       # esto SÍ es una copia real

# Listas anidadas (2D)
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[0][1])      # 2 - fila 0, columna 1

# Eliminar duplicados (tu lab)
unique = []
for number in my_list:
    if number not in unique:
        unique.append(number)