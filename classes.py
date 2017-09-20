students = []


class Student:

    school_name = "G.W. Smith Elementary"

    def __init__(self, name, student_id=332): # init is a constructor method. initialization.
        self.name = name
        self.student_id = student_id
        students.append(self)


    def __str__(self): #method override.. string
        return "Student " + self.name


    def get_name_capitalize(self):
        return self.name.capitalize()


    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student): #derived class(parent class)

    school_name = "Hunting Hills High School"


    def get_school_name(self):
        return "This is a High School student."


    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"

james = HighSchoolStudent("james")
print(james.get_name_capitalize())