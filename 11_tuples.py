# TUPLES - PE1 Module 4
# Como listas pero INMUTABLES - no se pueden cambiar

# Crear tupla
my_tuple = (1, 2, 3, 4, 5)
single = (1,)          # coma obligatoria para una sola
empty = ()

# Indexing y slicing igual que listas
print(my_tuple[0])     # 1
print(my_tuple[-1])    # 5
print(my_tuple[1:3])   # (2, 3)

# NO puedes modificar
# my_tuple[0] = 10  # → TypeError!

# Útiles para datos que no deben cambiar
coordinates = (14.6349, -90.5069)  # Guatemala City

# Desempacar
a, b, c = (1, 2, 3)
print(a, b, c)

# len, min, max, sum funcionan igual
print(len(my_tuple))
print(min(my_tuple))

# Convertir entre lista y tupla
my_list = list(my_tuple)   # tupla → lista
back = tuple(my_list)      # lista → tupla