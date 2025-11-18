# Simple Calculator Program with Auto Menu Loop

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

while True:
    print("\n----- Simple Calculator -----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting... Thank you for using the calculator!")
        break  # loop theke ber hoye program sesh

    if choice not in ['1', '2', '3', '4']:
        print("Invalid Input! Please choose between 1 to 5.")
        continue  # abar menu dekhabe

    # ekhane ashlei dhore nilam user 1-4 er moddhe choice dise
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers!")
        continue

    if choice == '1':
        print("Result:", add(num1, num2))

    elif choice == '2':
        print("Result:", subtract(num1, num2))

    elif choice == '3':
        print("Result:", multiply(num1, num2))

    elif choice == '4':
        print("Result:", divide(num1, num2))
