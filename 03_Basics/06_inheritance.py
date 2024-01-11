# Scenerio:3
"""
Multiple parent class
single child class

<child inherit from multiple parent class>
==> Multi-Class Inheritance
"""


class father:
    def meth_father(self):
        print("This is father's class")


class mother:
    def meth_mother(self):
        print("This is mother's class")


# Inheriting from mother as well as father
class child(father, mother):
    def meth_child(self):
        print("TThis is child's Class")


# object of child
obj_child = child()
# obj_child.meth_father()
# obj_child.meth_mother()


# @Scenerio-4
"""
if both father and mother have common method name ho wto ensure which method we are calling from child class object
"""


class father:
    def test(self):
        print("This is father's class")


class mother:
    def test(self):
        print("This is mother's class")


# Inheriting from mother as well as father
class child(father, mother):
    def meth_child(self):
        print("TThis is child's Class")


# Creating Object of child class
object_child = child()
object_child.test()  # inheriting father noth mother depends on order : inheriting <MRO> : Method resolution order
