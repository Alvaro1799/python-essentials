# Ejercicios — Variables, tipos y operadores

> Temas: `input()`, `print()`, f-strings, `int()` / `float()` / `str()`, `type()`, operadores `+ - * / // % **`, `round()`.
> Archivo sugerido: `ejercicios/mis_soluciones/01_variables_*.py`

---

## Fácil — Ficha de perfil

**Qué practicas:** entrada de datos, casting y f-strings.

**Requisitos**
1. Pide al usuario tres datos con `input()`: nombre, edad y estatura en metros.
2. Guarda la edad como `int` y la estatura como `float` (usa casting explícito).
3. Calcula el año aproximado de nacimiento: `2026 - edad`.
4. Imprime **una sola línea** con f-string que incluya nombre, edad, estatura y año de nacimiento.
5. Imprime el tipo de cada una de las tres variables usando `type()`.

**Ejemplo de ejecución**
```
Nombre: Alvaro
Edad: 27
Estatura (m): 1.75

Alvaro tiene 27 años, mide 1.75 m y nació aproximadamente en 1999.
name -> <class 'str'>
age -> <class 'int'>
height -> <class 'float'>
```

**Pistas**
- `input()` siempre devuelve `str`, aunque el usuario escriba números.
- En f-strings puedes meter expresiones directamente: `f"{2026 - age}"`.

---

## Medio — Propina y división de cuenta

**Qué practicas:** operadores aritméticos, `round()`, precisión con dinero.

**Requisitos**
1. Pide: total de la cuenta (float), porcentaje de propina (int) y número de personas (int).
2. Calcula la propina y el total final (cuenta + propina).
3. Calcula cuánto paga cada persona, redondeado a 2 decimales con `round()`.
4. Calcula la **diferencia de redondeo**: `total_final - (pago_por_persona * personas)`. Muéstrala redondeada a 2 decimales.
5. Imprime todos los montos con exactamente 2 decimales usando f-string (`f"{value:.2f}"`).

**Ejemplo de ejecución**
```
Total de la cuenta: 247.80
Porcentaje de propina: 15
Número de personas: 7

Propina:        37.17
Total con propina: 284.97
Cada persona paga: 40.71
Diferencia por redondeo: 0.00
```

**Pistas**
- Porcentaje se aplica como `total * percent / 100`.
- Si la diferencia sale distinta de `0.00`, no está mal: significa que el redondeo dejó centavos sueltos. Eso es justo lo que quieres ver.

---

## Difícil — Conversor de tiempo + anatomía de un número

**Qué practicas:** división entera `//`, módulo `%`, formato con ceros a la izquierda.

### Parte A — Segundos a `Xd HHh MMm SSs`
**Requisitos**
1. Pide un número entero de segundos (puede ser grande, ej. 400000).
2. Conviértelo a días, horas, minutos y segundos usando **solo** `//` y `%`.
3. Imprime el resultado con horas, minutos y segundos siempre a 2 dígitos (`f"{value:02d}"`).
4. Los días **no** llevan ceros a la izquierda.

**Ejemplo**
```
Segundos: 400000
4d 15h 06m 40s
```

### Parte B — Dígitos de un número de 3 cifras
**Requisitos**
1. Pide un entero de exactamente 3 dígitos (asume que el usuario coopera, todavía no validas).
2. Extrae cada dígito usando **solo** `//` y `%`. Prohibido usar listas, loops, slicing o `str()`.
3. Imprime los tres dígitos por separado y su suma.
4. Indica si el número es capicúa (se lee igual al derecho y al revés) comparando el primer y el tercer dígito.

**Ejemplo**
```
Número de 3 dígitos: 484
Dígitos: 4 - 8 - 4
Suma: 16
¿Capicúa? True
```

**Pistas**
- `400000 // 86400` te da los días; `400000 % 86400` te deja lo que sobra para seguir.
- Para el dígito del centro: quítale las centenas y luego quítale las unidades.

---

## Reto extra (opcional)
Combina ambas partes: pide segundos, muestra el formato de tiempo y además la suma de todos los dígitos del número original — esta vez sí puedes usar un loop.
