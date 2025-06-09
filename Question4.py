import json

students = [
    {"name": "John", "grade": 85},
    {"name": "Tim", "grade": 75},
    {"name": "Tom", "grade": 65},
    {"name": "Mary", "grade": 55}
]

def display():
    print("Student grade manager")
    print("1 :add a student")
    print("2 :Display students")
    print("3 :Search for student")
    print("4 :Calculate data")
    print("5 :Save data")
    print("6 :Load data")
    print("7 :exit")


def add_student():
    name = input("Enter a student name: ")
    grade = int(input("Enter the student grade: "))

    if name != "" and grade >= 0:
        students.append({"name": name, "grade": grade})
        print("Student added")
    else:
        print("Enter valid information")
    save_data()
    
def display_all_students():
    if not students:
        print("No students to display.")
    else:
        print("\n--- Student Records ---")
        for student in students:
            print(f"Name: {student['name']}, Grade: {student['grade']}")


def search_student():
    name = input("Enter name to search: ")
    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Found: {student['name']} - Grade: {student['grade']}")
            found = True
            break
    if not found:
        print("Name not found.")

def calculate_statistics():
    if not students:
        print("No student data to calculate.")
        return

    total = 0
    highest = students[0]["grade"]
    lowest = students[0]["grade"]

    for student in students:
        grade = student["grade"]
        total += grade
        if grade > highest:
            highest = grade
        if grade < lowest:
            lowest = grade

    average = total / len(students)

    print(f"\nAverage Grade: {average:.2f}")
    print(f"Highest Grade: {highest}")
    print(f"Lowest Grade: {lowest}")


def save_data():
    with open("file.txt", "w") as f:
        json.dump(students, f)
    print("Data saved successfully.")

def load_data():
    global students
    try:
        with open("file.txt", "r") as f:
            students = json.load(f)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No saved file found.")

def main():
    while True:
        display()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_student()
            print("")
        elif choice == "2":
            display_all_students()
            print("")
        elif choice == "3":
            search_student()
            print("")
        elif choice =="4":
            calculate_statistics()
            print("")
        elif choice =="5":
            save_data()
            print("")
        elif choice == "6":
            load_data()
            print("")
        elif choice == "7":
            break

if __name__ == "__main__":
    main()












