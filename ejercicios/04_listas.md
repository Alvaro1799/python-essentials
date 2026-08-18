# Ejercicios — Listas

> Temas: indexado, slicing, mutabilidad, `append()` / `insert()` / `del` / `remove()`, `len()`, `in`, `sorted()` vs `.sort()`, copia vs referencia, listas de listas, bubble sort, list comprehensions.
> Archivo sugerido: `ejercicios/mis_soluciones/04_listas_*.py`

---

## Fácil — Lista de compras

**Qué practicas:** operaciones básicas de lista y el operador `in`.

**Requisitos**
1. Empieza con una lista vacía.
2. Pide productos al usuario en un loop hasta que escriba `fin`.
3. Si el producto ya está en la lista, avísale y **no lo agregues** dos veces.
4. Al terminar imprime:
   - la lista completa,
   - cuántos productos hay,
   - el primero y el último,
   - la lista ordenada alfabéticamente **sin modificar la original** (demuéstralo imprimiendo las dos).
5. Pide un producto a eliminar; si existe, bórralo e imprime la lista final; si no, di que no estaba.

**Ejemplo de ejecución**
```
Producto (o 'fin'): huevos
Producto (o 'fin'): leche
Producto (o 'fin'): huevos
Ya está en la lista.
Producto (o 'fin'): pan
Producto (o 'fin'): fin

Lista: ['huevos', 'leche', 'pan']
Total: 3
Primero: huevos | Último: pan
Ordenada: ['huevos', 'leche', 'pan']
Original intacta: ['huevos', 'leche', 'pan']

¿Qué eliminas?: leche
Lista final: ['huevos', 'pan']
```

**Pistas**
- `sorted(lista)` devuelve una lista nueva; `lista.sort()` modifica la original. Aquí necesitas la primera.
- `lista[-1]` es el último elemento sin tener que calcular `len() - 1`.

---

## Medio — Estadísticas de notas (a mano)

**Qué practicas:** recorrer listas, acumuladores, slicing y comprehensions.

**Requisitos**
1. Pide cuántas notas va a ingresar el usuario y luego pide esa cantidad de notas (guárdalas como `float`).
2. Calcula **con tus propios loops** (prohibido `sum()`, `max()`, `min()`): total, promedio, nota más alta y nota más baja.
3. Cuenta cuántas notas están por encima del promedio e imprime cuáles son.
4. Imprime las 3 notas más altas usando `sorted()` + slicing.
5. Usando una **list comprehension**, crea una lista con las notas convertidas a escala 0–10 (divididas entre 10) y muéstrala.

**Ejemplo de ejecución**
```
¿Cuántas notas? 5
Nota 1: 88
Nota 2: 45
Nota 3: 92
Nota 4: 71
Nota 5: 63

Total: 359.0
Promedio: 71.80
Más alta: 92.0 | Más baja: 45.0
Sobre el promedio: 2 -> [88.0, 92.0]
Top 3: [92.0, 88.0, 71.0]
Escala 0-10: [8.8, 4.5, 9.2, 7.1, 6.3]
```

**Pistas**
- Para el máximo a mano: arranca asumiendo que el primer elemento es el mayor y compara contra el resto.
- `sorted(notas, reverse=True)[:3]` te da el top 3 en una línea.
- Comprehension: `[n / 10 for n in notas]`.

---

## Difícil — Ranking de jugadores con bubble sort

**Qué practicas:** listas de listas, bubble sort manual, copia vs referencia, formato de salida.

**Requisitos**
1. Parte de esta lista de listas (cópiala tal cual a tu archivo):
   ```python
   players = [
       ["Alvaro", 1240],
       ["Cindy", 1890],
       ["Marco", 1240],
       ["Lucía", 2310],
       ["Ana", 980],
   ]
   ```
2. Haz una **copia real** de `players` (no una referencia) y ordena la copia de mayor a menor puntaje con **bubble sort escrito por ti**. Prohibido `sorted()` y `.sort()` en esta parte.
3. Cuenta cuántos intercambios hizo el algoritmo e imprímelo.
4. Imprime el ranking en formato de tabla: posición, nombre y puntaje alineados.
5. Si hay empate en puntaje, ambos comparten posición (ej. dos jugadores en el puesto 3, y el siguiente pasa al puesto 5).
6. Al final, imprime la lista original para demostrar que **no** se modificó.
7. Imprime el promedio de puntos y quiénes están por encima de él.

**Ejemplo de ejecución**
```
Intercambios realizados: 4

#   Jugador    Puntos
1   Lucía      2310
2   Cindy      1890
3   Alvaro     1240
3   Marco      1240
5   Ana        980

Original sin tocar: [['Alvaro', 1240], ['Cindy', 1890], ['Marco', 1240], ['Lucía', 2310], ['Ana', 980]]
Promedio: 1532.0
Sobre el promedio: Lucía, Cindy
```

**Pistas**
- Ojo: `copia = players[:]` copia la lista externa, pero las sublistas siguen siendo las mismas en memoria. Si solo reordenas las sublistas (sin modificarlas por dentro) te sirve; si las modificas, necesitas copiar cada sublista también. Piénsalo y decide.
- En bubble sort comparas `copia[i][1]` contra `copia[i+1][1]` — el `[1]` es el puntaje.
- El conteo de 4 intercambios asume que solo intercambias cuando el siguiente es **estrictamente mayor** (los empates no se tocan). Si tu número sale distinto, revisa esa comparación.
- Para las posiciones con empate: la posición no es "el contador del loop", es "cuántos jugadores tienen más puntos que este, más uno".
- Alineación en f-strings: `f"{name:<10}"` alinea a la izquierda en 10 espacios.

---

## Reto extra (opcional)
Convierte el ranking en un tablero: una lista de listas 3x3 donde vas colocando los primeros 9 nombres, e imprímelo como cuadrícula con loops anidados.
