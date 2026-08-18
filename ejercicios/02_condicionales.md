# Ejercicios — Condicionales

> Temas: `if` / `elif` / `else`, operadores de comparación, `and` / `or` / `not`, condiciones anidadas.
> Archivo sugerido: `ejercicios/mis_soluciones/02_condicionales_*.py`

---

## Fácil — Clasificador de notas

**Qué practicas:** cadena `if` / `elif` / `else` y validación de rango.

**Requisitos**
1. Pide una nota como número entero (0 a 100).
2. Si la nota está fuera del rango 0–100, imprime `Nota inválida` y no hagas nada más.
3. Si es válida, asigna la letra según la escala:
   - 90–100 → `A`
   - 80–89 → `B`
   - 70–79 → `C`
   - 60–69 → `D`
   - 0–59 → `F`
4. Imprime la letra y además `Aprobado` si la nota es 60 o más, o `Reprobado` si no.

**Ejemplo de ejecución**
```
Nota: 84
Letra: B
Aprobado
```
```
Nota: 105
Nota inválida
```

**Pistas**
- Aprovecha el orden del `elif`: si ya sabes que no es ≥ 90, no necesitas escribir `nota < 90` otra vez.

---

## Medio — Cotizador de envío

**Qué practicas:** condiciones anidadas y operadores lógicos combinados.

**Requisitos**
1. Pide tres datos: peso del paquete en kg (float), destino (`local`, `nacional` o `internacional`) y total de la compra en Q (float).
2. Calcula la tarifa base según el destino:
   - `local` → Q25
   - `nacional` → Q45
   - `internacional` → Q120
   - cualquier otra cosa → imprime `Destino no reconocido` y termina.
3. Recargo por peso: si el paquete pesa más de 5 kg, suma Q10 por cada kg completo por encima de 5.
4. Envío gratis si el total de la compra es Q500 o más **y** el destino no es internacional.
5. Imprime el desglose: tarifa base, recargo, y total a pagar (o `Envío gratis`).

**Ejemplo de ejecución**
```
Peso (kg): 7.4
Destino: nacional
Total de compra: 320

Tarifa base: Q45.00
Recargo por peso: Q20.00
Total envío: Q65.00
```
```
Peso (kg): 2
Destino: local
Total de compra: 640

Envío gratis
```

**Pistas**
- "Q10 por cada kg completo arriba de 5" con 7.4 kg da 2 kg completos → Q20. Piensa en `int()` o `//`.
- La regla de envío gratis se evalúa **después** de calcular todo, o antes: tú decides el orden, pero que se note en el código cuál gana.

---

## Difícil — Validador de fechas

**Qué practicas:** lógica combinada, reglas de negocio reales, condiciones excluyentes.

**Requisitos**
1. Pide día, mes y año como enteros.
2. Determina si la fecha es válida. Reglas:
   - Mes entre 1 y 12.
   - Año mayor a 1582.
   - Días según el mes: 31 para enero, marzo, mayo, julio, agosto, octubre, diciembre; 30 para abril, junio, septiembre, noviembre; febrero depende del año.
   - Año bisiesto: divisible entre 4, **excepto** si es divisible entre 100, **salvo** que también sea divisible entre 400.
3. Si es válida, imprime `Fecha válida` y si el año es bisiesto o no.
4. Si es inválida, imprime **el motivo específico**: mes fuera de rango, año fuera de rango, o día inválido para ese mes (indicando cuántos días tiene ese mes).
5. Restricción: resuélvelo con condicionales. Nada de listas, diccionarios ni `datetime` todavía.

**Ejemplo de ejecución**
```
Día: 29
Mes: 2
Año: 2024
Fecha válida — 2024 es año bisiesto.
```
```
Día: 29
Mes: 2
Año: 1900
Fecha inválida: febrero de 1900 tiene 28 días.
```
```
Día: 31
Mes: 4
Año: 2026
Fecha inválida: abril tiene 30 días.
```

**Pistas**
- Calcula primero `days_in_month` con condicionales, y **después** compara contra el día. Es más limpio que meter la comparación en cada rama.
- La regla de bisiesto en orden: `% 400` → sí; si no, `% 100` → no; si no, `% 4` → sí; si no, no.
- 1900 no es bisiesto, 2000 sí. Úsalos como casos de prueba.

---

## Reto extra (opcional)
Agrega el cálculo del día del año (de 1 a 366): cuántos días han pasado desde el 1 de enero hasta la fecha ingresada.
