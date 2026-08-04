# for interaction
def user():
    user_selector = input("What do you want us to run Today?")
    if user_selector == "Odd":
        odd_numbers()
    elif user_selector == "Even":
        even_numbers()
    else:
        print("Please say Even/even or Odd/odd, to proceed.")
        
           
# for odd
def odd_numbers():
    limit = get_limit()
    for i in range(1, limit + 1):
        if i % 2 != 0: #not equal to %2 for odd
            print(i)
        else:
            continue

# for even
def even_numbers():
    limit = get_limit()
    for i in range(1, limit + 1):
        if i % 2 == 0: #not equal to %2 for even
            print(i)
        else:
            continue

# for limit
def get_limit():
    return int(input("Please provide the limit number for your request: "))

user()