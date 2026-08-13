'''Ejercicios de refuerzo: listas, indexacion e if/and/or dentro de funciones

Estos ejercicios practican los mismos conceptos usados en 11_functionslab2.py:
- crear una lista dentro de una funcion
- indexar una lista con un offset (ajustar +1/-1)
- combinar condiciones con "and" / "or"
- devolver None cuando los argumentos no tienen sentido

Completa cada funcion donde dice "Escribe tu codigo aqui". Cada ejercicio
tiene su propio bloque de pruebas debajo.
'''

# ---------------------------------------------------------------------------
# Ejercicio 1: Indexacion con offset
#
# Dada la lista de nombres de dias, escribe nombre_dia(n) que reciba un
# numero de dia ISO (1=Lunes ... 7=Domingo) y devuelva el nombre
# correspondiente. Si n esta fuera de 1-7, devuelve None.
# ---------------------------------------------------------------------------

def nombre_dia(n):
    dias_semana = ["Lun", "Mar", "Mier", "Jue", "Vie", "Sab", "Dom"]
    if n < 1 or n > 7:
        return None
    return dias_semana[n - 1]

test_n = [1, 7, 3, 0, 8]
test_esperado = ["Lun", "Dom", "Mier", None, None]
for i in range(len(test_n)):
    n = test_n[i]
    resultado = nombre_dia(n)
    print(n, "->", resultado, "OK" if resultado == test_esperado[i] else "Failed")


# ---------------------------------------------------------------------------
# Ejercicio 2: Validacion + lista + rangos
#
# Escribe precio_entrada(edad) que devuelva el precio segun el rango:
#   nino (0-12), adulto (13-64), adulto mayor (65+)
# usando una lista de precios [5, 10, 15].
# Si edad < 0, devuelve None.
# ---------------------------------------------------------------------------

def precio_entrada(edad):
    precios = [5, 10, 15]
    #
    # Escribe tu codigo aqui
    #

test_edades = [5, 12, 13, 40, 64, 65, 90, -1]
test_esperado2 = [5, 5, 10, 10, 10, 15, 15, None]
for i in range(len(test_edades)):
    edad = test_edades[i]
    resultado = precio_entrada(edad)
    print(edad, "->", resultado, "OK" if resultado == test_esperado2[i] else "Failed")


# ---------------------------------------------------------------------------
# Ejercicio 3: Combinar dos condiciones con "or"
#
# Escribe es_dia_laboral_festivo(dia_semana, es_festivo) que devuelva False
# si dia_semana es "Sab" o "Dom", O si es_festivo es True. En cualquier otro
# caso devuelve True.
# ---------------------------------------------------------------------------

def es_dia_laboral_festivo(dia_semana, es_festivo):
    #
    # Escribe tu codigo aqui
    #

test_dias = ["Lun", "Sab", "Dom", "Mar", "Jue"]
test_festivo = [False, False, False, True, False]
test_esperado3 = [True, False, False, False, True]
for i in range(len(test_dias)):
    dia = test_dias[i]
    fest = test_festivo[i]
    resultado = es_dia_laboral_festivo(dia, fest)
    print(dia, fest, "->", resultado, "OK" if resultado == test_esperado3[i] else "Failed")
