def main():
    stps = 0
    c0 = int(input("Give me your number: "))
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 // 2
            print(c0)
            stps += 1
        else:
            c0 = 3 * c0 + 1
            print(c0)
            stps += 1
    print ("Total steps: " + str(stps))
main()
