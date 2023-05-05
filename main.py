import sys

# to compare valid choices
choices = ["1", "2", "3", "4", "5", "6", "7", "8"]


# is Integer method to validate input is integer
def is_integer(num):
    try:
        num = int(num)

    except ValueError:
        return False

    return True


# is number method to validate input is number
def is_number(num):
    try:
        num = float(num)

    except ValueError:
        return False

    return True


# used to read grades text fil
def read_file(filename):
    students = {}
    with open(filename, "r") as file:
        for line in file:
            student_data = line.strip().split("#")
            student_id = student_data[0].strip()
            student_name = student_data[1].strip()
            grades = list(map(float, student_data[2].strip().split()))
            students[student_id] = {"name": student_name, "grades": grades}
    return students


# writing on text file
def save_file(filename, students):
    with open(filename, "w") as file:
        for student_id, student_data in students.items():
            line = student_id + "# " + student_data["name"] + "# " + " ".join(
                str(grade) for grade in student_data["grades"])
            file.write(line + "\n")


def print_heading(students):
    # format method print data in proper alignment
    print("{:20}{:35}".format("StudentID", "Student Name"), end="")

    for i in range(1, len(list(students.values())[0]["grades"]) + 1):
        print("{:9}".format("Test " + str(i)), end="")
    print()


def print_info(student_id, student_data):
    print("{:20}{:30}".format(student_id, student_data["name"]), end="")
    for grade in student_data["grades"]:
        print("{:9}".format(grade), end="")
    print()


# used to print all data of text file on console
def display_all_students(students):
    print_heading(students)

    for student_id, student_data in students.items():
        print_info(student_id, student_data)


# displaying a particular student selected
def display_student(students, student_id):
    if student_id not in students:
        print("Error: Invalid student ID")
    else:
        student_data = students[student_id]
        print("{:20}{:35}".format("StudentID", "Student Name"), end="")

        for i in range(1, len(list(students.values())[0]["grades"]) + 1):
            print("{:9}".format("Test " + str(i)), end="")
        print()

        print("{:20}{:30}".format(student_id, student_data["name"]), end="")
        for grade in student_data["grades"]:
            print("{:9}".format(grade), end="")
        print()


# print student info with average score
def display_averages(students):
    print("{:20}{:30}{}".format("StudentID", "Student Name", "Average"))
    for student_id, student_data in students.items():
        # calculating average score
        average = sum(student_data["grades"]) / len(student_data["grades"])
        print("{:20}{:30}{:.1f}".format(student_id, student_data["name"], average))


# modify result as per new info
def modify_grade(students, student_id, test_num, new_grade):

    # before Modification
    print("\nBefore grade modification:")
    print_heading(students)

    # printing previous data
    student_data = students[student_id]
    print_info(student_id, student_data)

    # updating grade
    student_data["grades"][test_num - 1] = new_grade

    # After Modification
    print("\nAfter grade modification:")
    print_heading(students)

    # printing previous data
    student_data = students[student_id]
    print_info(student_id, student_data)
    print()


# adding new grades for all students
def add_test_grades(students):
    print("Please enter test grades for Test#{}".format(len(list(students.values())[0]["grades"]) + 1))
    for student_id, student_data in students.items():

        # input grades for every student and validating it
        while True:
            if is_number(grade := input("Please enter grade for student {}: ".format(student_id))):
                grade = float(grade)
                if 0 <= grade <= 100:
                    student_data["grades"].append(grade)
                    students[student_id] = student_data
                    break

                else:
                    print("Error: Invalid grade")
            else:
                print("Error: Invalid grade")


# adding new student
def add_student(students, student_id, student_name):
    count = len(list(students.values())[0]["grades"])
    st_grade = []
    for i in range(count):
        st_grade.append(0)

    if student_id in students:
        print("Error: Student with the same ID already exists")
    else:
        students[student_id] = {"name": student_name, "grades": st_grade}


# delete chosen student
def delete_student(students, student_id):
    if student_id not in students:
        print("Error: Invalid student ID")
    else:
        del students[student_id]


def main():
    # reading info of all students and storing
    filename = "grades.txt"
    students = read_file(filename)

    # continuously display options and operation to perform
    while True:
        print("\n")
        print("1. Display Grade Info for all students")
        print("2. Display Grade Info for a particular student")
        print("3. Display tests average for all students")
        print("4. Modify a particular test grade for a particular student")
        print("5. Add test grades for a particular test for all students")
        print("6. Add a new Student")
        print("7. Delete a student")
        print("8. Save and Exit")

        # take input until user gives us a valid choice (1 to 8)
        while (choice := input("\nPlease select your choice: ")) not in choices:
            print("Invalid choice (you can choose only 1 to 8)")

        choice = int(choice)

        if choice == 1:
            display_all_students(students)

        elif choice == 2:
            student_id = input("Enter studentID: ")
            display_student(students, student_id)

        elif choice == 3:
            display_averages(students)

        elif choice == 4:

            # studentID input and validation of input
            while (student_id := input("Please enter studentID: ")) not in students:
                print("StudentID#" + str(student_id) + " not exist")

            # input test number and validating it
            while True:
                if is_integer(test_num := input("Please enter quiz number to modify: ")):
                    test_num = int(test_num)
                    if test_num < 1 or test_num > len(list(students.values())[0]["grades"]):
                        print("Error: Invalid quiz number")
                    else:
                        break
                else:
                    print("Error: Invalid quiz number")

            # input test number and validating it
            while True:
                if is_number(new_grade := input("Please enter new quiz {} grade: ".format(test_num))):
                    new_grade = float(new_grade)
                    if new_grade < 0 or new_grade > 100:
                        print("Error: Invalid grade")
                    else:
                        break
                else:
                    print("Error: Invalid grade")

            modify_grade(students, student_id, test_num, new_grade)

        elif choice == 5:
            add_test_grades(students)

        elif choice == 6:
            student_id = input("Enter studentID: ")
            student_name = input("Enter student name: ")
            add_student(students, student_id, student_name)

        elif choice == 7:
            student_id = input("Enter studentID: ")
            delete_student(students, student_id)

        elif choice == 8:
            save_file(filename, students)
            print("Data saved. Exiting...")
            sys.exit(0)

        else:
            print("Invalid choice, please try again.")

        # showing message(press Enter to continue) until user presses Enter key
        while continueChoice := input("Press Enter key to continue . . .") != "":
            pass


main()
