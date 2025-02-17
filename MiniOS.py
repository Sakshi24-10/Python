import os

# Calculator functions
def add(Num1, Num2): 
    return Num1 + Num2

def sub(Num1, Num2):
    return Num1 - Num2

def multi(Num1, Num2):
    return Num1 * Num2

def div(Num1, Num2):
    if Num2 == 0:
        return "Error: Division by zero is not allowed."
    return Num1 / Num2

while True:
    print("\nMiniOS")
    print("Select an option from below:")
    print("1. Login ")
    print("2. File manager")
    print("3. Calculator")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nLogin")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        # Save username and password (not secure, should use encryption/hashing)
        with open("Myfile.txt", "a") as f:
            f.write(f"Username: {username}, Password: {password}\n")

    elif choice == 2:
        print("\nFile Manager")
        print("1. Create File ")
        print("2. Delete File ")
        print("3. Read File ")
        
        x = int(input("Enter your choice: "))  

        if x == 1:
            filename = input("Enter a file name: ")
            with open(filename, "w") as file:
                print(f"File '{filename}' created successfully.")

        elif x == 2:
            filename = input("Enter the file name to delete: ")
            if os.path.exists(filename):
                os.remove(filename)
                print(f"File '{filename}' deleted successfully.")
            else:
                print("Error: File does not exist.")

        elif x == 3:
            filename = input("Enter the file name to read: ")
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    print("\nFile contents:\n", file.read())
            else:
                print("Error: File does not exist.")

    elif choice == 3:
        print("\nCalculator")
        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        value = int(input("Enter your choice: "))
        Num1 = float(input("Enter first number: "))
        Num2 = float(input("Enter second number: "))

        if value == 1:
            print("Result:", add(Num1, Num2))
        elif value == 2:
            print("Result:", sub(Num1, Num2))
        elif value == 3:
            print("Result:", multi(Num1, Num2))
        elif value == 4:
            print("Result:", div(Num1, Num2))
        else:
            print("Invalid choice.")

    elif choice == 4:
        print("Exiting MiniOS...")
        break

    else:
        print("Invalid choice. Please enter a valid option.")