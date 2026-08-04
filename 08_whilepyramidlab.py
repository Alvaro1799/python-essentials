blocks = int(input("Enter the number of blocks: "))
userh = 0
currenth = 1

while blocks >= currenth:
    blocks -= currenth
    userh += 1
    currenth += 1
    


print("The height of the pyramid:", userh)

