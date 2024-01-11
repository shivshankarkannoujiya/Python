class mentor:
    class_var = 10

    def __init__(self, mentor_name, mentor_email):
        self._mentor_name = mentor_name
        self.__mentor_email = mentor_email

    def print_mentor_details(self):
        print(self._mentor_name, self.__mentor_email)


"""
default : public
single _ : Protected >>> EX:- _mentor_name
"""

# Creating instance
obj_mentor = mentor("Abhi", "abhi@gmail.com")

# @Access protected property
# Use single _ as we written inside the class
print(obj_mentor._mentor_name)


"""
Private : double (__) underscore
Can access inside class using : __
but not outside of Class through object
Eg: __mentor_email
"""

# @Accessing [private] property
# we have to provide the [_className] with property

# Ex:
print(obj_mentor._mentor__mentor_email)