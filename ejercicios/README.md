# Ejercicios de práctica — PE1

Ejercicios propios para repasar todo lo visto en **Cisco Python Essentials 1**, ahora que el curso está terminado y antes de entrar de lleno a PE2.

**Un documento por categoría, tres niveles en cada uno:** Fácil → Medio → Difícil.
Cada ejercicio trae qué concepto practica, requisitos numerados, un ejemplo de ejecución esperado y pistas — **no soluciones**. La idea es que los resuelvas tú.

| # | Documento | Temas |
|---|---|---|
| 1 | [01_variables_operadores.md](01_variables_operadores.md) | `input()`, casting, f-strings, `//` `%` `**`, `round()` |
| 2 | [02_condicionales.md](02_condicionales.md) | `if` / `elif` / `else`, `and` / `or` / `not`, anidamiento |
| 3 | [03_loops.md](03_loops.md) | `while`, `for`, `range()`, `break`, `continue`, loops anidados |
| 4 | [04_listas.md](04_listas.md) | indexado, slicing, métodos, copia vs referencia, bubble sort, listas de listas, comprehensions |
| 5 | [05_funciones.md](05_funciones.md) | `def`, `return`, parámetros por defecto, scope, recursión |
| 6 | [06_tuplas_diccionarios.md](06_tuplas_diccionarios.md) | tuplas inmutables, dicts, dicts anidados, iteración |
| 7 | [07_excepciones.md](07_excepciones.md) | `try` / `except` / `else` / `finally`, `raise`, tipos de error |

## Cómo trabajarlos

1. Escribe tu solución en `mis_soluciones/` con el nombre que sugiere cada doc, por ejemplo `mis_soluciones/03_loops_medio.py`.
2. Corre el archivo y compara la salida contra el **ejemplo de ejecución** del doc — ese es tu criterio de "listo".
3. Lee las pistas solo si te trabas más de 10 minutos. Están escritas para empujarte, no para resolverte el ejercicio.
4. Commit pequeño por ejercicio terminado (`git add` del archivo + mensaje tipo `Loops nivel medio resuelto`).

**Sugerencia de ritmo:** un nivel por sesión de 30 min. Los "difícil" están pensados para tomar dos sesiones — son los que de verdad combinan varios temas a la vez.

## Restricciones a propósito

Varios ejercicios prohíben atajos (`sum()`, `max()`, `[::-1]`, `sorted()` en ciertas partes). No es por dificultad gratuita: es para que escribas el loop a mano una vez y entiendas qué hace el built-in por dentro. Después ya puedes usarlos con confianza.
