# Class-Declaration
class test:
    pass


# class-2
class pwskills:
    course = "python"

    # self : is not reserved keyword can take anything
    def welcome_msg(self):
        print("Welcome to pwskills")


# creating instance/object/class variable
# b -> is instance of pwskills class
b = pwskills()

# Accessing method and property
b.welcome_msg()
print(b.course)
