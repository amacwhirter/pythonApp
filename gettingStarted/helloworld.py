print("Hello World")

# ///////IF STATEMENTS\\\\\\\\

number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is NOT 5")

text = "Python"
if text:
    print("Text is defined and truthy")

python_course = True
if python_course: # Not python_course == True
    print("This will execute")

python_course = True
if not python_course: # Not python_course == True
    print("This will NOT execute.")

aliens_found = None
if aliens_found:
    print("This will NOT execute")

number = 3
python_course = True
if number == 3 and python_course:
    print("This will execute")

if number == 17 or python_course:
    print("This will also execute.")

#///////Lists\\\\\\\\\

student_names = ["Mark", "Katarina", "Jessica"]
student_names[0] == "Mark"
student_names[2] == "Jessica"
student_names[-1] == "Jessica"
student_names.append("Homer")
"Mark" in student_names == True #Mark is still there!
#len(student_list) == 4 # How many elements in the list

#deleting index in list
del student_names[2]

#slicing list
student_names = ["Mark", "Katarina", "Jessica"]
student_names[1:] == ["Katrina", "Homer"]
student_names[1:-1] == ["Katrina"]

#//////Loops\\\\\\\\\\

#for loop
for name in student_names:
    print("Student name is {0}" .format(name))

#/////Break and Continue\\\\\\

student_names = ["James", "Katarina", "Jessica", "Mark", "Bort", "Frank Grimes", "Max Power"]

for name in student_names:
    if name == "Mark":
        print("Found him! " + name)
        break #Stop iteration once wanted result found.
    print("Currently testing " + name)

for name in student_names:
    if name == "Bort":
        continue #Skips over mentioned iteration and continues.
    print("Currently testing " + name)

#/////While Loops\\\\\\ repeat itself while condition is true.

# num = 10
# while True:
#     if num == 42:
#         break
#     print("Hello World")

#/////Dictionaries\\\\\\\

#Dictionaries are useful when it comes to storing some kind of structured data.

student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

# Grouping multiple dictionaries - create list of dictionaries.

all_students = [
    {"name": "Mark", "student_id": 15163 },
    {"name": "Katarina", "student_id": 63112 },
    {"name": "Jessica", "student_id": 30021 }
]

# student["name"] == "Mark"
# student["last_name"] == KeyError
# student.get("last_name", "Unknown") == "Unknown"
# student.keys() = ["name", "student_id", "feedback"]
# student.values() = ["Mark", 15163, None]
# student["name"] = "James"
# del student["name"]

#////////Exceptions\\\\\\\\

student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

try:
    last_name = student["last_name"]
except KeyError:
    print("Error finding last_name")

print("This code executes")

student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

student["last_name"] = "Kowalski"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last_name")
except TypeError as error:  # as error tells more specifics about error thrown.
    print("I can't add these two together!")
    print(error)
except Exception:  # handles any error that is not specifically handled above.
    print("Unknown Error.")

print("This code executes")

#///////Other Data Types\\\\\\\\\

complex  # complex numbers

long  # only in python 2 (replaced by integer in 3)

bytes and bytearray  # integers in the range of 0 to 255, a sequence of strings or other objects, etc.

tuple = (3, 5, 1, "Mark")  # immutable -- cannot change their values

set and frozenset  # similar to list but only have unique objects.

set([3, 2, 3, 1, 5]) == (1, 2, 3, 5)  # got rid of duplicates and ordered the list

