hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

get_replacement = int(input("What is your replacement for hats?"))
hat_list[2] = get_replacement

del hat_list[-1]

print("\nNew list length: ", len(hat_list))
print("\n", hat_list)

