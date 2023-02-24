import string, random

# characters list --> contain our random password character:
# list constructor
characters = list(string.hexdigits + string.ascii_letters + string.digits + '!@#$%^&*()')

def Random_password_generator():
    pass_lenght = int(input("Enter your required password lenght?: "))
    random.shuffle(characters)
    # password list --> contain our random password
    password = []

    for i in range(pass_lenght):
        password.append(random.choice(characters))


    random.shuffle(password)

    # password is list --> convert into string
    password = "".join(password)                # join method --> iterably take all items in list/tuple and join them into string
                                                # "".join(password)--> iterably take all items from password --> and join them with no space
                                                 # "#".join(password)---> iterably take all items from password --> and join them with #
    print(type(password))
    print(password)

if __name__ == '__main__':
    option = input('Do you want to generate random password: (Yes/No): ')
    if option.lower() == 'yes' or option.lower() == 'y':
        Random_password_generator()
    elif option.lower() == 'no':
        print('programe terminate')
        quit()
    else:
        print("wrong input , please enter (Yes or No")


