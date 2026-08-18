# Ejercicios — Loops

> Temas: `while`, `for`, `range()`, `break`, `continue`, `else` en loops, loops anidados.
> Archivo sugerido: `ejercicios/mis_soluciones/03_loops_*.py`

---

## Fácil — Tabla de multiplicar y suma de pares

**Qué practicas:** `for` con `range()` y acumuladores.

**Requisitos**
1. Pide un número entero `n` al usuario.
2. Imprime la tabla de multiplicar de `n` del 1 al 10, una línea por resultado, con formato `n x i = resultado`.
3. Después, recorre del 1 al `n` y acumula la suma de **solo los números pares**.
4. Imprime cuántos pares encontró y la suma total.

**Ejemplo de ejecución**
```
Número: 6
6 x 1 = 6
6 x 2 = 12
...
6 x 10 = 60

Pares del 1 al 6: 3
Suma de pares: 12
```

**Pistas**
- `range(1, 11)` va del 1 al 10 — el límite superior nunca se incluye.
- Un acumulador arranca en 0 **antes** del loop, nunca adentro.

---

## Medio — Adivina el número con intentos limitados

**Qué practicas:** `while`, `break`, `continue` y validación de entrada.

**Requisitos**
1. Define un número secreto entre 1 y 100 (fíjalo tú en el código por ahora).
2. El usuario tiene **6 intentos** para adivinarlo.
3. En cada intento:
   - Si lo que escribió no es un número (usa `.isdigit()`), imprime `Eso no es un número` y **no le descuentes el intento** (`continue`).
   - Si el número está fuera de 1–100, avísale y tampoco le descuentes el intento.
   - Si es muy alto o muy bajo, dile cuál de los dos y cuántos intentos le quedan.
   - Si acierta, felicítalo diciendo en qué intento lo logró y sal del loop con `break`.
4. Si se le acaban los intentos, revela el número secreto.
5. Al final imprime siempre un resumen: intentos usados y si ganó o no.

**Ejemplo de ejecución**
```
Adivina el número (1-100). Tienes 6 intentos.
Intento: 50
Muy alto. Te quedan 5 intentos.
Intento: abc
Eso no es un número.
Intento: 25
Muy bajo. Te quedan 4 intentos.
Intento: 37
¡Correcto! Lo lograste en 3 intentos.
```

**Pistas**
- Si `continue` salta la línea que descuenta el intento, el usuario no pierde nada por escribir mal. Ordena tu loop pensando en eso.
- Considera `while attempts_left > 0:` en lugar de un `for`, para tener control fino de cuándo descuentas.

---

## Difícil — Analizador de texto sin atajos

**Qué practicas:** recorrer strings, loops anidados, construir un resultado carácter por carácter.

**Requisitos**
1. Pide una frase al usuario.
2. Recorre la frase y cuenta: vocales, consonantes, dígitos, espacios y otros caracteres. Imprime las 5 cuentas.
3. Construye e imprime la frase **invertida** usando un loop. Prohibido usar `[::-1]` y `reversed()`.
4. Determina si la frase es palíndroma ignorando espacios, signos y mayúsculas. Imprime `True` o `False`.
5. Imprime la palabra más larga de la frase. Prohibido usar `.split()`: recórrela carácter por carácter y detecta los espacios tú mismo.

**Ejemplo de ejecución**
```
Frase: Anita lava la tina 2026

Vocales: 8
Consonantes: 7
Dígitos: 4
Espacios: 4
Otros: 0

Invertida: 6202 anit al aval atinA
¿Palíndroma? False
Palabra más larga: Anita
```
```
Frase: A man, a plan, a canal: Panama

¿Palíndroma? True
```

**Pistas**
- Para invertir: recorre normal y ve poniendo cada carácter **al inicio** del acumulador (`result = char + result`).
- Para "la palabra más larga" sin `split()`: lleva un contador de la palabra actual y una copia de la mejor encontrada; cuando topes un espacio, cierra la palabra actual. No olvides cerrar la última palabra al terminar el loop.
- Para el palíndromo, primero construye una versión limpia de la frase (solo letras, en minúsculas) y luego compárala con su inversa.

---

## Reto extra (opcional)
Imprime un histograma de las 5 vocales con asteriscos, usando loops anidados:
```
a: *****
e: **
i: ***
```
