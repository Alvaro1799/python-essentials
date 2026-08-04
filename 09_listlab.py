import time

beatles = []
print("Step 1:", beatles)

beatles.append('John_Lennon')
beatles.append('Paul_McCartney')
beatles.append('George_Harrison')
print("Step 2:", beatles)

for i in range(2):
    i += 1
    input1 = input("Please add Stu Sutcliffe to the band: ")
    print("Adding ", {input1})
    time.sleep(1)
    beatles.append(input1)
    input2 = input("Thank you, now please add Pete Best to the band: ")
    print("Adding ", {input2})
    time.sleep(1)
    beatles.append(input2)

print("Step 3:", beatles)

print("Removing", {beatles[4]})
del beatles[4]
time.sleep(0.5)
print("Removing", {beatles[3]})
del beatles[3]
time.sleep(0.5)
print("Step 4:", beatles)

beatles.insert(0, "Ringo_Star")
print("Step 5:", beatles)

print("The Fab", len(beatles))

