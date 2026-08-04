import time

user_word = input("Type your word:")
scrt = "chupacabra"

while user_word != scrt:
    print("Your word is " + user_word + " And..")
    time.sleep(2)
    print("you are still in the loop")
    user_word = input("Type your word:")

print("Your word is " + user_word + " And..")
time.sleep(2)
print("Te has salido del loop!!")
