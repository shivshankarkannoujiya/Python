# sets_1 = {}
# print(type(sets_1)) #<class 'dict'>

"""
1. set are not ordered
2. Do not have indexing
3. Does not contain Duplicate value
"""
setOne = {"Abhishek", "happy", "Ajay", "Shiivam"}
# print(type(setOne))
# print(setOne)

setTwo = {"Abhi", "shivam", "ashish", 12, True, 1}
# print(setTwo)


# 1
# @Accessing
# Can access using loop
"""
for i in setTwo:
    print(i)
"""

# 2
# @Adding<.add()>
setTwo.add("lav")
# print(setTwo)

# @update
setTwo.update(("Veer",))
# passing as tuple also can pass list
# print(setTwo)

# @union
# setTwo.union("Vivek")
# print([setTwo])  # not working

# @Remove
# if value is not present : Throw Error
setTwo.remove("Veer")
# print(setTwo)

# @discard
# if value is not present then : Does not throw Error
setTwo.discard("ashish")
# print(setTwo)

# @pop()
# Randomly remove any value
setTwo.pop()
# print(setTwo)

# @clear()
# clear all the values
setTwo.clear()
print(setTwo)  # set()
