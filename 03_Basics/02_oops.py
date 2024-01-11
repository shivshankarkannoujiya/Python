class pwskills1:
    def __init__(self, course, duration, mentor):
        self.course = course
        self.duration = duration
        self.mentor = mentor

    def show_mentor(self):
        print("print mentor name : ", self.mentor)


"""
__init__
1. it is inbuilt method : [ctor]
2. Provide data to class
"""

# Creating instance-1
# now we have to pass arguments : due to ctor
dsm = pwskills1("DSM", 9, "Abhi")

# instance-2
jdsd = pwskills1("JDSD", 6, "Shiv")


# @Printing the values
# here : Indirecttly we are calling the {self.course}
# if we change the name {self.course1} then we hav to call like
# dsm.course1
print(dsm.course)
print(dsm.duration)
print(jdsd.course)
print(jdsd.duration)

# priinting mentor of dsm and jdsd 
dsm.show_mentor()
jdsd.show_mentor()