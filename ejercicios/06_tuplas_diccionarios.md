# Ejercicios — Tuplas y diccionarios

> Temas: tuplas (inmutables, empaquetado/desempaquetado), diccionarios (`keys()`, `values()`, `items()`, `get()`, `del`, `in`), diccionarios anidados, iteración.
> Archivo sugerido: `ejercicios/mis_soluciones/06_tuplas_dicts_*.py`

---

## Fácil — Agenda de contactos

**Qué practicas:** crear, leer, actualizar y borrar en un diccionario.

**Requisitos**
1. Empieza con este diccionario:
   ```python
   contacts = {"Cindy": "5555-1234", "Marco": "4444-9876"}
   ```
2. Agrega dos contactos nuevos pedidos al usuario (nombre → teléfono).
3. Actualiza el teléfono de un contacto existente.
4. Busca un contacto con `.get()` de modo que si no existe imprima `No encontrado` en lugar de reventar.
5. Borra un contacto con `del`, pero **solo** si existe (usa `in` para verificar).
6. Imprime al final: la agenda completa recorriendo `.items()`, cuántos contactos hay, y la lista de nombres ordenada alfabéticamente.

**Ejemplo de ejecución**
```
Nombre: Ana
Teléfono: 3333-1111

Actualizar teléfono de: Cindy
Nuevo teléfono: 5555-9999

Buscar: Pedro
No encontrado
Buscar: Cindy
Cindy -> 5555-9999

Borrar: Marco
Marco eliminado.

=== AGENDA (3) ===
Ana: 3333-1111
Cindy: 5555-9999
Lucía: 2222-8888
```

**Pistas**
- `contacts["Pedro"]` truena si la key no existe; `contacts.get("Pedro")` devuelve `None`. Esa es la diferencia clave de este ejercicio.
- `sorted(contacts.keys())` te da los nombres ordenados sin tocar el diccionario.

---

## Medio — Contador de palabras

**Qué practicas:** construir un diccionario dinámicamente y recorrerlo buscando máximos.

**Requisitos**
1. Pide una frase al usuario y sepárala en palabras con `.split()`.
2. Normaliza cada palabra: minúsculas y sin signos de puntuación (`, . ! ? ;`).
3. Construye un diccionario `palabra → cuántas veces aparece`.
4. Imprime el diccionario completo, una palabra por línea.
5. Encuentra e imprime la palabra más repetida **recorriendo el diccionario con un loop** (sin `max()`).
6. Imprime cuántas palabras aparecen una sola vez.
7. Usa una **tupla** para guardar el resultado final: `(palabra_más_repetida, veces)` y demuestra que es inmutable intentando modificarla (comenta esa línea con el error que da).

**Ejemplo de ejecución**
```
Frase: el gato y el perro y el pez

el: 3
gato: 1
y: 2
perro: 1
pez: 1

Palabra más repetida: ('el', 3)
Palabras únicas: 3
```

**Pistas**
- El patrón clásico: `if word in counter: counter[word] += 1 else: counter[word] = 1`. También existe `counter.get(word, 0) + 1` — pruébalo y quédate con el que entiendas mejor.
- Para el máximo a mano: guarda `best_word` y `best_count`, y ve comparando mientras recorres `.items()`.
- Al intentar `resultado[0] = "otro"` obtendrás `TypeError: 'tuple' object does not support item assignment`. Ese error es parte de la respuesta.

---

## Difícil — Inventario con diccionarios anidados

**Qué practicas:** diccionarios de diccionarios, tuplas como registros inmutables, funciones + estructuras de datos juntas.

**Requisitos**
1. Parte de este inventario:
   ```python
   inventory = {
       "chocochip":  {"price": 18.0, "stock": 24, "min_stock": 10},
       "red_velvet": {"price": 22.0, "stock": 6,  "min_stock": 10},
       "oreo":       {"price": 20.0, "stock": 15, "min_stock": 8},
   }
   ```
2. Escribe estas funciones:
   - `sell(inventory, product, quantity)` → si el producto no existe o no hay stock suficiente, imprime el motivo y retorna `None`. Si sí, descuenta el stock y retorna una **tupla** `(producto, cantidad, total_cobrado)`.
   - `restock(inventory, product, quantity)` → suma stock; si el producto no existe, lo crea pidiendo precio y stock mínimo.
   - `inventory_value(inventory)` → retorna el valor total (precio × stock de todos los productos).
   - `low_stock(inventory)` → retorna una **lista de tuplas** `(producto, stock, min_stock)` de los productos por debajo de su mínimo.
   - `show_inventory(inventory)` → imprime la tabla completa marcando con ⚠ los productos bajos.
3. Guarda todas las ventas en una lista `sales` (lista de tuplas). Al final imprime: número de ventas, total facturado y el producto más vendido.
4. Menú con `while`: 1) vender, 2) reabastecer, 3) ver inventario, 4) ver alertas de stock bajo, 5) cerrar caja (imprime el resumen y sale).
5. Las ventas ya registradas **no se pueden modificar** — por eso son tuplas. No conviertas la lista de ventas en listas de listas.

**Ejemplo de ejecución**
```
Opción: 1
Producto: red_velvet
Cantidad: 8
No hay stock suficiente de 'red_velvet' (disponible: 6).

Opción: 1
Producto: red_velvet
Cantidad: 4
Venta registrada: ('red_velvet', 4, 88.0)

Opción: 3
Producto      Precio   Stock   Mín
chocochip     Q18.00   24      10
red_velvet    Q22.00   2       10   ⚠
oreo          Q20.00   15      8

Valor del inventario: Q776.00

Opción: 5
=== CIERRE DE CAJA ===
Ventas: 3
Total facturado: Q216.00
Producto más vendido: chocochip (6 unidades)
```

**Pistas**
- Acceder a un valor anidado: `inventory["oreo"]["stock"]`. Para modificarlo es igual, con `=`.
- Para "el producto más vendido", construye otro diccionario `producto → unidades` recorriendo `sales`, y luego busca el máximo a mano.
- `low_stock()` retorna datos, no imprime. `show_inventory()` imprime, no calcula. Mantén esa separación — es el mismo principio del doc de funciones.

---

## Reto extra (opcional)
Agrega `apply_discount(inventory, percent)` que retorne un **diccionario nuevo** con los precios rebajados, sin modificar el original. Comprueba que el inventario original quedó intacto.
