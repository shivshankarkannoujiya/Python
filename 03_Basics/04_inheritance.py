# Scenerio-1 :
"""
Parent amd child class have method of <same name>
we want to call parent method with child class
==> <Method Overriding>
"""


# Parent
class xyz:
    def test(self):
        print("This is part of xyz class")


# child
class child(xyz):
    def test(self):
        super().test()
        print("This is part of child class")


# Want to access parent-method
# child_class_obj
obj_child = child()
# obj_child.test()  # Unable to call method of parent

# using super().test() in chils class method we can access both
obj_child.test()
