names = ["John", "Mary", "Tom", "Shawn"]

def display():
    print("--Options--")
    print("1: Concatenate two strings")
    print("2: Convert string to uppercase")
    print("3: Convert string to lowercase")
    print("4: Exit")

def show_names():
    print("\nAvailable names:")
    for i, name in enumerate(names):
        print(f"{i}: {name}")

def concatenate():
    show_names()
    try:
        i = int(input("Enter the index of the first name: "))
        j = int(input("Enter the index of the second name: "))
        print("Result:", names[i] + names[j])
    except (IndexError, ValueError):
        print("Invalid index input")

def uppercase():
    show_names()
    try:
        i = int(input("Enter the index of the name to convert to uppercase: "))
        print("Result:", names[i].upper())
    except (IndexError, ValueError):
        print("Invalid index input")

def lower():
    show_names()
    try:
        i = int(input("Enter the index of the name to convert to lowercase: "))
        print("Result:", names[i].lower())
    except (IndexError, ValueError):
        print("Invalid index input")

def main():
    while True:
        display()

        choice = input("Choose one of the above: ")

        if choice == "1":
            concatenate()
        elif choice == "2":
            uppercase()
        elif choice == "3":
            lower()
        elif choice == "4":
            break
        else:
            print("Error")

if __name__ == "__main__":
    main()


