# Ejercicios — Excepciones

> Temas: `try` / `except` / `else` / `finally`, excepciones específicas (`ValueError`, `ZeroDivisionError`, `IndexError`, `KeyError`, `TypeError`), `raise`, jerarquía de excepciones.
> Archivo sugerido: `ejercicios/mis_soluciones/07_excepciones_*.py`

---

## Fácil — Input a prueba de balas

**Qué practicas:** `try` / `except ValueError` dentro de un loop.

**Requisitos**
1. Pide al usuario un número entero.
2. Si escribe algo que no se puede convertir, atrapa el `ValueError`, imprime `Eso no es un número entero, intenta otra vez` y vuelve a preguntar.
3. Repite hasta obtener un entero válido.
4. Cuando lo obtengas, imprime su doble y su cuadrado.
5. Usa `else` en el `try` para el código que solo debe correr si la conversión salió bien, y `finally` para imprimir `Intento registrado` después de cada vuelta.

**Ejemplo de ejecución**
```
Número entero: hola
Eso no es un número entero, intenta otra vez.
Intento registrado.
Número entero: 3.5
Eso no es un número entero, intenta otra vez.
Intento registrado.
Número entero: 12
Intento registrado.
Doble: 24 | Cuadrado: 144
```

**Pistas**
- `int("3.5")` también lanza `ValueError`. Ese es el segundo caso del ejemplo.
- El `finally` corre pase lo que pase: con error, sin error, e incluso si haces `break`.

---

## Medio — Calculadora que no se cae

**Qué practicas:** varios `except` distintos, capturar el error como variable, orden de las excepciones.

**Requisitos**
1. Pide dos números y un operador (`+`, `-`, `*`, `/`, `//`, `%`, `**`).
2. Maneja **por separado**:
   - `ValueError` → el usuario no escribió un número.
   - `ZeroDivisionError` → intentó dividir entre cero.
   - Operador no soportado → **lánzalo tú** con `raise ValueError("Operador no soportado: ...")` y atrápalo.
3. Captura el error como variable (`except ValueError as e`) e imprime el mensaje real de Python, no solo el tuyo.
4. Agrega un `except Exception as e` **al final** como red de seguridad, e imprime también `type(e).__name__`.
5. Envuelve todo en un loop que permita hacer varias operaciones hasta que el usuario escriba `salir`. Usa `finally` para imprimir una línea separadora después de cada operación.

**Ejemplo de ejecución**
```
Número 1: 10
Número 2: 0
Operador: /
Error de división: division by zero
--------------------

Número 1: 10
Número 2: abc
Operador: +
Error de valor: invalid literal for int() with base 10: 'abc'
--------------------

Número 1: 7
Número 2: 3
Operador: ^
Error de valor: Operador no soportado: ^
--------------------

Número 1: 2
Número 2: 10
Operador: **
Resultado: 1024
--------------------
```

**Pistas**
- El orden importa: `except Exception` atrapa **todo**, así que si lo pones primero los demás nunca se ejecutan. Va siempre al final.
- Nota que tu propio `raise ValueError(...)` cae en el mismo `except ValueError` que el input inválido. Si quieres distinguirlos, tendrías que separar los `try`. Pruébalo de las dos formas y decide cuál lees mejor.

---

## Difícil — Validador de registros con errores propios

**Qué practicas:** `raise`, funciones que lanzan excepciones, recolectar errores sin detener el programa, excepciones anidadas.

**Requisitos**
1. Parte de esta lista de registros (algunos están mal a propósito):
   ```python
   records = [
       {"name": "Alvaro", "age": "27",  "email": "alvaro@mail.com"},
       {"name": "",       "age": "31",  "email": "cindy@mail.com"},
       {"name": "Marco",  "age": "abc", "email": "marco@mail.com"},
       {"name": "Lucía",  "age": "-5",  "email": "lucia@mail.com"},
       {"name": "Ana",    "age": "22",  "email": "ana-mail.com"},
       {"name": "Pedro",  "age": "40"},
   ]
   ```
2. Escribe `validate(record)` que **lance** una excepción con mensaje claro cuando algo esté mal:
   - nombre vacío → `raise ValueError("El nombre no puede estar vacío")`
   - edad no numérica → deja que reviente el `ValueError` del `int()`, pero atrápalo y relánzalo con un mensaje más claro
   - edad fuera de 0–120 → `raise ValueError(...)`
   - email sin `@` o sin `.` → `raise ValueError(...)`
   - falta la key `email` → `raise KeyError(...)` (o deja que el acceso al dict lo lance)
   - Si todo está bien, retorna el registro con la edad ya convertida a `int`.
3. Recorre todos los registros dentro de un loop con `try` / `except`. **Un registro malo no debe detener el proceso.**
4. Acumula dos listas: `valid` (registros correctos) e `invalid` (tuplas `(nombre_o_indice, tipo_de_error, mensaje)`).
5. Al final imprime un reporte: cuántos válidos, cuántos inválidos, y el detalle de cada error con su tipo (`ValueError`, `KeyError`, etc.).
6. Imprime el porcentaje de registros válidos, protegiendo la división contra una lista vacía.

**Ejemplo de ejecución**
```
=== VALIDACIÓN ===
✔ Alvaro (27)
✘ registro #2 — ValueError: El nombre no puede estar vacío
✘ Marco — ValueError: La edad 'abc' no es un número entero
✘ Lucía — ValueError: La edad -5 está fuera del rango 0-120
✘ Ana — ValueError: Email inválido: 'ana-mail.com'
✘ Pedro — KeyError: Falta el campo 'email'

Válidos: 1 | Inválidos: 5
Tasa de validez: 16.67%
```

**Pistas**
- Para relanzar con mejor mensaje: `try: age = int(...) except ValueError: raise ValueError(f"La edad '{...}' no es un número entero")`.
- `type(e).__name__` te da `"ValueError"` o `"KeyError"` como texto, justo lo que necesitas para el reporte.
- El registro #2 no tiene nombre, así que en el reporte tienes que identificarlo por su índice. Usa `enumerate(records, start=1)`.
- Cuidado con `except Exception` aquí: quieres saber **qué** falló, no solo que falló.

---

## Puente a PE2 (opcional)
En PE2 vas a ver clases. Cuando llegues, vuelve a este ejercicio y crea tus propias excepciones:
```python
class InvalidRecordError(Exception):
    pass
```
y reemplaza los `ValueError` genéricos por errores con nombre propio. Vas a notar de inmediato por qué existen.
