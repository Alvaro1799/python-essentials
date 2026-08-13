# DICTIONARIES - PE1 Module 4
# Pares key:value, no ordenados, mutables

# Crear diccionario
person = {
    "name": "Alvaro",
    "age": 27,
    "city": "Guatemala"
}

# Acceder por key
print(person["name"])        # Alvaro
print(person.get("age"))     # 27 - más seguro

# Agregar y modificar
person["job"] = "Team Lead"  # agregar
person["age"] = 28           # modificar

# Eliminar
del person["city"]

# Métodos útiles
print(person.keys())         # todas las keys
print(person.values())       # todos los valores
print(person.items())        # pares (key, value)

# Iterar
for key, value in person.items():
    print(key + ":", value)

# Verificar si key existe
if "name" in person:
    print("Existe!")

# Diccionario de diccionarios
team = {
    "alvaro": {"role": "lead", "years": 7},
    "cindy": {"role": "translator", "years": 3}
}
print(team["alvaro"]["role"])  # lead