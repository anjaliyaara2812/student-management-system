def add_student():
    file = open("students.txt", "a")
    sid = input("Enter student ID: ")
    name = input("Enter name: ")
    course = input("Enter course: ")
    marks = input("Enter marks: ")
    file.write(sid + "," + name + "," + course + "," + marks + "\n")
    file.close()
    print("Student added successfully")


def view_students():
    try:
        file = open("students.txt", "r")
        print("\nStudent List:")
        for line in file:
            data = line.strip().split(",")
            print("ID:", data[0], "Name:", data[1], "Course:", data[2], "Marks:", data[3])
        file.close()
    except:
        print("No student record found")


def update_student():
    sid = input("Enter student ID to update: ")
    file = open("students.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("students.txt", "w")
    found = False

    for line in lines:
        data = line.strip().split(",")
        if data[0] == sid:
            name = input("Enter new name: ")
            course = input("Enter new course: ")
            marks = input("Enter new marks: ")
            file.write(sid + "," + name + "," + course + "," + marks + "\n")
            found = True
        else:
            file.write(line)

    file.close()

    if found:
        print("Student updated successfully")
    else:
        print("Student ID not found")


def delete_student():
    sid = input("Enter student ID to delete: ")
    file = open("students.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("students.txt", "w")
    found = False

    for line in lines:
        data = line.strip().split(",")
        if data[0] != sid:
            file.write(line)
        else:
            found = True

    file.close()

    if found:
        print("Student deleted successfully")
    else:
        print("Student ID not found")


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
