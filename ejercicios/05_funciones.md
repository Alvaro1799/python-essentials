# Ejercicios — Funciones

> Temas: `def`, parámetros posicionales y con nombre, valores por defecto, `return`, `None`, scope local vs global, `global`, recursión.
> Archivo sugerido: `ejercicios/mis_soluciones/05_funciones_*.py`

---

## Fácil — Conversores de temperatura

**Qué practicas:** `def`, `return` y parámetros con valor por defecto.

**Requisitos**
1. Escribe `celsius_to_fahrenheit(celsius)` que **retorne** el valor (no que lo imprima). Fórmula: `c * 9/5 + 32`.
2. Escribe `fahrenheit_to_celsius(fahrenheit)` que retorne el valor. Fórmula: `(f - 32) * 5/9`.
3. Escribe `show_temperature(value, unit="C")` que imprima la temperatura formateada a 1 decimal con su unidad.
4. Prueba las tres funciones con al menos 3 valores cada una, incluyendo el punto de congelación (0 °C) y el punto donde ambas escalas coinciden (-40).
5. Verifica en tu prueba que convertir de ida y vuelta devuelve el valor original.

**Ejemplo de ejecución**
```
0.0 C -> 32.0 F
100.0 C -> 212.0 F
-40.0 C -> -40.0 F
98.6 F -> 37.0 C
Ida y vuelta: 25 C -> 77.0 F -> 25.0 C ✔
```

**Pistas**
- Una función que solo hace `print()` retorna `None`. Aquí quieres `return` para poder encadenar conversiones.
- El default `unit="C"` significa que `show_temperature(30)` funciona sin segundo argumento.

---

## Medio — Caja de herramientas de validación

**Qué practicas:** funciones que retornan booleanos, reutilizar unas funciones dentro de otras.

**Requisitos**
1. `is_prime(n)` → `True` si `n` es primo, `False` si no. Ojo con 0, 1 y negativos.
2. `count_vowels(text)` → cuántas vocales tiene el texto (sin importar mayúsculas).
3. `is_strong_password(password)` → `True` solo si cumple **todas** estas reglas:
   - mínimo 8 caracteres,
   - al menos una mayúscula,
   - al menos una minúscula,
   - al menos un dígito.
4. `password_report(password)` → **usa** `is_strong_password()` y `count_vowels()`, e imprime un reporte con cada regla marcada ✔ o ✘.
5. Prueba `password_report()` con al menos 3 contraseñas distintas: una fuerte, una corta y una sin dígitos.

**Ejemplo de ejecución**
```
Primos del 1 al 20: 2 3 5 7 11 13 17 19

Contraseña: guatemala
  Largo >= 8    ✔
  Mayúscula     ✘
  Minúscula     ✔
  Dígito        ✘
  Vocales: 5
  Resultado: DÉBIL

Contraseña: Coolkies2026
  Largo >= 8    ✔
  Mayúscula     ✔
  Minúscula     ✔
  Dígito        ✔
  Vocales: 4
  Resultado: FUERTE
```

**Pistas**
- Para `is_prime`, basta con probar divisores hasta la raíz de `n` (`while i * i <= n`). No necesitas llegar hasta `n`.
- Métodos útiles de string: `.isupper()`, `.islower()`, `.isdigit()` sobre cada carácter.
- Cuando una regla falla, puedes hacer `return False` de inmediato. No necesitas seguir revisando.

---

## Difícil — Mini sistema de gastos

**Qué practicas:** funciones que reciben y devuelven listas, scope, un menú con `while`, y recursión.

**Requisitos**
1. Los gastos se guardan en una lista de listas: `[categoría, descripción, monto]`.
2. Escribe estas funciones (cada una hace **una sola cosa**):
   - `add_expense(expenses, category, description, amount)` → agrega y retorna la lista actualizada.
   - `total_expenses(expenses)` → retorna el total gastado.
   - `total_by_category(expenses, category)` → retorna el total de una categoría.
   - `biggest_expense(expenses)` → retorna el gasto más caro (la sublista completa), o `None` si la lista está vacía.
   - `show_report(expenses)` → imprime el reporte completo. Esta es la única que imprime.
3. Menú en un `while` con opciones: 1) agregar gasto, 2) ver reporte, 3) buscar por categoría, 4) salir. Valida opciones inválidas.
4. Ninguna función excepto `show_report()` debe imprimir nada, y ninguna debe usar variables globales. Todo entra por parámetros y sale por `return`.
5. **Parte recursiva:** escribe `sum_recursive(numbers)` que sume una lista de montos **sin usar loops ni `sum()`** — solo llamándose a sí misma. Úsala como verificación cruzada de `total_expenses()` e imprime si ambos coinciden.

**Ejemplo de ejecución**
```
1) Agregar  2) Reporte  3) Buscar categoría  4) Salir
Opción: 1
Categoría: comida
Descripción: almuerzo
Monto: 65

Opción: 2
=== REPORTE DE GASTOS ===
comida    | almuerzo        | Q65.00
transporte| uber al trabajo | Q40.00
comida    | café            | Q22.50
-------------------------
Total: Q127.50
Gasto más caro: almuerzo (Q65.00)
Verificación recursiva: Q127.50 ✔

Opción: 3
Categoría a buscar: comida
Total en 'comida': Q87.50 (2 gastos)
```

**Pistas**
- El caso base de la recursión es la lista vacía → retorna 0. El caso recursivo es `numbers[0] + sum_recursive(numbers[1:])`.
- Si te tienta escribir `global expenses`, párate: pásala como parámetro y reasigna con el `return`. Ese es el punto del ejercicio.
- `biggest_expense()` retornando `None` te obliga a manejar el caso "todavía no hay gastos" en `show_report()`.

---

## Reto extra (opcional)
Agrega `filter_expenses(expenses, min_amount)` usando una **list comprehension** en una sola línea, que retorne solo los gastos por encima de cierto monto.
