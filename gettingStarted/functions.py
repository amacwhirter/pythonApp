students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):

    """
    Adds the student to the student list.
    :param name: string - student name
    :param student_id: integer - optional student ID
    :return:
    """
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")  # 'a' denotes wanting to append to file. 'w' will overwrite any information.
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file.")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


# def var_args(name, **kwargs):
#     print(name)
#     print(kwargs["description"], kwargs["feedback"], kwargs["pluralsight_subscriber"])


# var_args("Mark", description="Loves Python", feedback=None, pluralsight_subscriber=True)

read_file()
print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(student_name, student_id)
save_file(student_name)


#///Nested Function\\\

# def get_students():
#     students = ["mark", "james"]
#     def get_students_titlecase = []
#         students_titlecase = []
#         for student in students:
#             students_titlecase.append(student.title())
#         return student_titlecase
#     students_titlecase_names = get_students_titlecase()
#     print(students_titlecase_names)


#///Lambda Functions\\\
# from
# def double (x):
#     return x * 2
#
# to
# double = lambda x: x * 2
# ==> double(5) == 10
#
# Lambda functions are useful in higher-order functions which are regular functions in Python that actually take another function as their argument.
