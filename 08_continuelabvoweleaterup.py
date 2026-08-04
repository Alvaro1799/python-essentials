# Prompt the user to enter a word
user_word = input("Choose your word:")
user_word = user_word.upper()
vowels = ("A" , "E", "I", "O", "U")
word_without_vowels = ""

# look for vowels and assigned them to var
for letter in user_word:
    if letter in vowels: 
        word_without_vowels += letter 
        continue
    else:
        print(letter)

print("The vowels eaten were: " + word_without_vowels + " YUMMY!!")

