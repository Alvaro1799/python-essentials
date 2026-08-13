# Práctica: funciones con return y listas
# Basado en 10_functionssummary2.py
# Instrucciones: escribe el código debajo de cada ejercicio.
# NO hay matemáticas. Prometido. :)

# ---------------------------------------------------------------
# Ejercicio 1 — return básico
# Escribe una función llamada `saludo` que RECIBA un nombre (string)
# y DEVUELVA (return, no print) el string "Hola, <nombre>!".
# Luego llámala con tu nombre e imprime el resultado.
# Ejemplo esperado de salida: Hola, Alvaro!


# ---------------------------------------------------------------
# Ejercicio 2 — return sin valor
# Escribe una función llamada `despedida` que imprima "Adiós!"
# y después tenga solo `return` (sin valor).
# Llama a la función así:  print(despedida())
# ANTES de correrlo, escribe en un comentario qué crees que va a
# imprimir y por qué. Luego corre y compara.


# ---------------------------------------------------------------
# Ejercicio 3 — guardar el resultado en una variable
# Escribe una función `menu_del_dia` que devuelva el string de tu
# comida favorita. Guarda el resultado en una variable llamada
# `comida` y luego imprime: "Hoy toca: <comida>"
# (pista: usa la variable dentro del print, no llames la función
# dos veces)


# ---------------------------------------------------------------
# Ejercicio 4 — lista como argumento
# Escribe una función `invitar` que reciba una lista de nombres
# e imprima para cada uno: "<nombre>, estás invitado!"
# Prueba con esta lista:
invitados = ["Cindy", "Carlos", "Marta"]


# ---------------------------------------------------------------
# Ejercicio 5 — la función DEVUELVE una lista
# Escribe una función `lista_de_palabras` que reciba un número n
# y devuelva una lista con n strings "cookie".
# Ejemplo: lista_de_palabras(3) -> ["cookie", "cookie", "cookie"]
# Imprime el resultado de llamarla con 4.
# (pista: es como create_list del summary, pero en vez de agregar
# i, agregas el string)


# ---------------------------------------------------------------
# Ejercicio 6 (reto) — combina todo
# Escribe una función `etiquetar` que reciba una lista de nombres
# y DEVUELVA una NUEVA lista donde cada nombre tenga el prefijo
# "Invitado: ". No imprimas nada dentro de la función.
# Luego, fuera de la función, recorre la lista devuelta con un for
# e imprime cada etiqueta.
# Ejemplo: etiquetar(["Ana", "Luis"]) -> ["Invitado: Ana", "Invitado: Luis"]


# ===============================================================
# PARTE 2 — Recursión (basado en 10_functionssumary3.py)
# Recuerda: toda función recursiva necesita un CASO BASE
# (condición que detiene las llamadas) o nunca termina.
# ===============================================================

# ---------------------------------------------------------------
# Ejercicio 7 — cuenta regresiva con palabras
# Escribe una función RECURSIVA `cuenta_regresiva(n)` que imprima
# "Faltan <n>..." y se llame a sí misma con n - 1.
# Caso base: cuando n llega a 0, imprime "¡Despegue!" y NO se
# vuelve a llamar.
# Prueba con cuenta_regresiva(3). Salida esperada:
# Faltan 3...
# Faltan 2...
# Faltan 1...
# ¡Despegue!
# (pista: la estructura es if/else como el factorial del summary,
# pero en vez de multiplicar, imprimes)


# ---------------------------------------------------------------
# Ejercicio 8 (reto) — repetir una palabra con recursión
# Escribe una función RECURSIVA `repetir(palabra, n)` que DEVUELVA
# un string con la palabra repetida n veces separada por espacios.
# Ejemplo: repetir("cookie", 3) -> "cookie cookie cookie"
# Caso base: si n es 1, devuelve la palabra sola.
# Si no: devuelve la palabra + " " + repetir(palabra, n - 1)
# Imprime el resultado con repetir("galleta", 4)
# ANTES de correrlo: escribe en un comentario, paso a paso, qué
# devuelve cada llamada (como hicimos con 4 * 3 * 2 * 1 del
# factorial, pero con strings).
