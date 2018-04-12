



# a = 1
# b = 2
# print("bigger" if a>b else "smaller")
# print(len("jorgen"))

# student_name = ["Mark", "Katarina", "Jessica", "Homer"]
# del student_name[2]
# print(student_name)

# for student in student_name:
#     print(student)

# x= 0
# for index in range(10): # range(start,stop -1, hopp)
#     x +=10
#     print ("The value ofX is {0}".format(x))

# student={
#     "name": "Mark",
#     "student": 15163
# }

# al_students=[
#     {
#     "name": "Mark",
#     "student": 15163
# },
# {
#     "name": "Katarina",
#     "student": 15134
# }
# ]

# student["name"] = "Mark"
# #Get all keys 
# student.keys()
# #Get all values
# student.values()
# #delete from dictionary
# del student["name"]

student={
    "name": "Mark",
    "student": 15163
}
student["last_name"] = "Kowaloski" 
try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last name")
except TypeError as error:
    print("I can't add these two together!")
    print(error)
except Exception:
    print("Unknown error")
print("This code executes!")
