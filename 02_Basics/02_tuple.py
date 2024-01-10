# immutable --> something that cannot be changed

# 1
t1 = ()  # <class 'tuple'>
# print(type(t1))

# 2
t2 = 1  # <class 'int'>
# print(type(t2))


# but
# 3
t3 = (1,)  # <class 'tuple'>
# print(type(t3))

tuple_1 = ("apple", "mango", "banana", "cherry")
# print(tuple_1)


# 1
# @printing Length
# print(len(tuple_1))

# 2
# @Accessing
# print(tuple_1[1])

# 3
# @ tuple to list
# tuple --> list

# tuple_1 = list(tuple_1)
# print(tupleToList)
# print(type(tupleToList))
# print(type(tuple_1))


# 4
# @immutable
# tuple_1[1] = "tiger"
# print(tuple_1)
# TypeError: 'tuple' object does not support item assignment


# 5
# @to change value
"""
Step-1 : convert >> [tuple --> list ]
step-2 : change the value 
step-3 : Again convert [list --> tuple]
"""
# Ex:
# step-1
tuple_1 = list(tuple_1)
# step-2
tuple_1[1] = "tiger"
# step-3
tuple_1 = tuple(tuple_1)
# print(tuple_1)


# 6
# @Adding two tuples
tuple_1 = ("apple", "mango", "banana", "cherry")
tuple_2 = ("orange", "brinjal")

addedTuples = tuple_1 + tuple_2
# print(addedTuples)

# 7
# @Assigning each fruits to differents variabls
tuple_1 = ("apple", "mango", "banana", "cherry")

fruit1, fruit2, fruit3, fruit4 = tuple_1
# print(tuple_1)
# print(fruit1)
# print(fruit2)
# print(fruit3)
# print(fruit4)

# 8
# @Duplicate the value of tuple
# Can multiply by no we wants it

# Ex:
print(tuple_1 * 4)
