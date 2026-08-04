# LOOPS - PE1 Module 3
# Los loops repiten código mientras se cumpla una condición

# While básico
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# While True + break
while True:
    user = input("Type 'exit' to stop: ")
    if user == "exit":
        break
    print("You said: " + user)

# For + range()
for i in range(5):
    print(i)              # 0 al 4

for i in range(1, 6):
    print(i)              # 1 al 5

for i in range(0, 10, 2):
    print(i)              # pares: 0,2,4,6,8

# For iterando un string
word = "Alvaro"
for letter in word:
    print(letter)

# Continue - salta la iteración
for i in range(10):
    if i % 2 == 0:
        continue          # salta los pares
    print(i)              # imprime solo impares

# In operator
vowels = ("A", "E", "I", "O", "U")
letter = "A"
print(letter in vowels)       # True
print(letter not in vowels)   # False