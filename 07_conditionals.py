# conditionals - PE1 Module 2
# permite que el codigo tome decisiones como en la vida real

# if basico
edad = 27
if edad >= 18:
    print("Eres mayor de edad")

# if / else
temperatura = 15
if temperatura >= 20:
    print("Hace calor")
else:
    print("Hace frio")

# if / elif / else
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy bien")
elif nota >= 70:
    print("Bien")
elif nota >= 60:
    print("Suficiente")
else:
    print("Insuficiente")

# Comparadores en condicionales
x = 10
if x > 5 and x < 15:
    print("x esta entre 5 y 15")

if x < 5 or x > 15:
    print("x esta fuera de 5 y 15")

if not x == 5:
    print("x no es igual a 5")

#if the_weather_is_good:
#    if nice_restaurant_is_found:
#        have_lunch()
#    else:
#        eat_a_sandwich()
#else:
#    if tickets_are_available:
#        go_to_the_theater()
#    else:
#        go_shopping()

#this use of the if statement is known as nesting; 
#remember that every else refers to the if which lies 
#at the same indentation level; 
#you need to know this to determine 
#how the ifs and elses pair up;

#consider how the indentation improves readability, 
#and makes the code easier to understand and trace.

#if the_weather_is_good:
#    go_for_a_walk()
#elif tickets_are_available:
#    go_to_the_theater()
#elif table_is_available:
#    go_for_lunch()
#else:
#    play_chess_at_home()

#sometimes called a cascade

