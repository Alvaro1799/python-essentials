my_list = []
unique_list = []
datanumber = 5

for i in range(5):
    usernumber = input(f"Please share numbers with me: ")
    datanumber -= 1
    print(f"{datanumber} slots remaining.")
    my_list.append(usernumber)

for number in my_list:
    if number not in unique_list:
        unique_list.append(number)

print(f"The list with unique numbers are: {unique_list}")