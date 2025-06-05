import json

students = [
    {"name,John, grade, 83"},
    {"name, Mary, grade, 75"},
    {"name, Tom, grade 50"},
    {"name, Shawn, grade, 30"}
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
    if name in students:
        print(name)
    else:
        print("Name not found")

def calculate_statistics():

    grades = [student["grade"] for student in students]
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)

    print(f"\nAverage Grade: {average:.2f}")
    print(f"Highest Grade: {highest}")
    print(f"Lowest Grade: {lowest}")

def save_data():
    with open("file.txt", "w") as f:
        f.write(students)

    f = open("file.txt", "r")
    print(f.read())

def load_data():
    file1 = open("file.txt", "w")
    file1.writelines(students)
    file1.close()

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












