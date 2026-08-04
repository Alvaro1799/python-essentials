for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    else:
       print(ch, end="") 

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")