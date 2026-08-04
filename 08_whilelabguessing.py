scrt = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

unbr = int(input("Guess the number:"))

while unbr != scrt:
    print("Haha you are stuck on my loop")
    unbr = int(input("Guess the number again:"))
    if unbr == scrt:
        print("Yes, finally, you got it!")