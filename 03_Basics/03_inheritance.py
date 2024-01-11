# parent class
class pwskills:
    def pwskills(self):
        print("This is pwskills method")


# child-class
# inheriting from parent
class student(pwskills):
    pass


# creating instance of student class
obj_student = student()
# pwskills method inside the student class
# obj_student.pwskills()


# @Another Ex:

# parent class


class mentor:
    def __init__(self, mentor_name, mentor_email):
        self.mentor_name = mentor_name
        self.mentor_email = mentor_email

    def print_mentor_details(self):
        print("Name : ", self.mentor_name, "Email : ", self.mentor_email)


# Want to access methods and property from parent class
# inheriting

# child-class


class dataScience_master(mentor):
    def print_dsm(self):
        print("This is my dsm class")


# creating object of dataScience_master class
# we have to pass argument bcz parent class have ctor
obj_dsm = dataScience_master("Abhi", "abc@gmail.com")


print(obj_dsm.mentor_name)
print(obj_dsm.mentor_email)
obj_dsm.print_dsm()

# Accessing method of parent-class
obj_dsm.print_mentor_details()
