def add(a, b):
    ans = a + b
    print(ans)
    print(str(a) + "+" + str(b) + "=" + str(ans) + "\n")

def sub(a, b):
    ans = a - b
    print(str(a) + "-" + str(b) + "=" + str(ans) + "\n")

def mul(a, b):
    ans = a * b
    print(str(a) + "*" + str(b) + "=" + str(ans) + "\n")

def div(a, b):
    ans = a / b
    print(str(a) + "/" + str(b) + "=" + str(ans) + "\n")


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Divison")
    print("E. Exit")
    choice = input("Enter your choice: ")


    if choice == 'a' or choice == 'A':
        print("Addition")
        value1 = int(input("Enter first value"))
        value2 = int(input("Enter 2nd value"))
        add(value1, value2)
    elif choice == 'b' or choice == 'B':
        print("Subtraction")
        value1 = int(input("Enter first value"))
        value2 = int(input("Enter 2nd value"))
        sub(value1, value2)
    elif choice == 'c' or choice == 'C':
        print("Multiplication")
        value1 = int(input("Enter first value"))
        value2 = int(input("Enter 2nd value"))
        mul(value1, value2)
    elif choice == 'd' or choice == 'D':
        print("Division")
        value1 = int(input("Enter first value"))
        value2 = int(input("Enter 2nd value"))
        div(value1, value2)
    elif choice == 'e' or choice == 'E':
        print("Programe Ended")
        quit()


