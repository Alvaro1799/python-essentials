import time

user_word1 = input("Type your word:")

scrt = "chupacabra"
scrt2 = "lolo"

while True:
    print("Your word is " + user_word1 + " And..")
    if user_word1 == scrt:
        break
    time.sleep(2)
    print("you are still in the loop")
    user_word1 = input("Type your word:")

    continue
user_word2 = input("You got the first one! Now type your second word:")
while user_word2 != scrt2:
        print("Your word is " + user_word2 + " And..")
        time.sleep(2)
        print("You are still in the loop")
        user_word2 = input("Type your second word:")
     

print("Your words are " + user_word1 + " and " + user_word2 + " And..")
time.sleep(2)
print("Te has salido del loop!!")
     

