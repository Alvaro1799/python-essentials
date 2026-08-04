
user_word = input("Choose your word:")
user_word = user_word.upper()
vowels = ("A" , "E", "I", "O", "U")

for letter in user_word:
    if letter in vowels:
        # es vocal
        continue
    else:
        print(letter)


