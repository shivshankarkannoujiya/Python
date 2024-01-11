# Scenerio-2:
"""
Have, single parent-class
two -> child-class
They both  want to inherit the Parent Class 
==> <Multiple inheritance>
"""


class parent:
    def meth_parent(self):
        print(" This is Parent Class")


class child_One(parent):
    def meth_child_One(self):
        print("This is part of childOne")


class child_Two(parent):
    def meth_child_Two(self):
        print("This is part of childTwo")


obj_child_One = child_One()
obj_child_Two = child_Two()

# Accessing method of Parent from both child
obj_child_One.meth_parent()
obj_child_Two.meth_parent()
