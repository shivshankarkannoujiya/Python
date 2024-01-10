# ============@creation============

# @Method-1 -> {ctor}
# listOne = list()
# print(listOne)  # []
# print(type(listOne))  # <class 'list'>


# @Method-2
# listTwo = []
# print(type(listTwo))  # <class 'list'>


# @index     0         1        2        3
list_1 = ["apple", "Mango", "Banana", "cherry"]
# @index     -4      -3       -2      -1

# print(list_1)  # ['apple', 'Mango', 'Banana']


# 1
# =====@Accessing=====
# print(list_1[index_Number])

# Ex:
# print(list_1[1])


# 2
# =====@Slicing=====
# print(list[startIndex:endIndex:stepValue])
# startIndex : included
# endIndex : excluded
# stepValue : default -> 1

# Ex:
# print(list_1[1:3])
# print(list_1[1:])
# print(list_1[:3])

# stepValue
# print(list_1[0:4:2])

# 3
# @isPresent
# print("Mango" in list_1)

# 4
# ===== @insertion <insert> =====
# list_1.insert(index,value)
# Value aage shift ho jata hai hai overwrite nhi krta

# Ex:
# list_1.insert(1, "litchi")
# print(list_1)


# 5
# ===== @insertAtEnd <append> =====
# list_1.append("value")

# Ex:
# list_1.append("banana")
# print(list_1)


# 6
# ===== @insert<list>AtEnd <extend> =====
# list_1.extend(list_2)

# EX:
# list_2 = ["Tiger", "Lion", "Cat"]
# list_1.extend(list_2)
# print(list_1)


# ===== @deletefromlist <remove> =====
# if duplicate : Remove the first Occurence
# list.remove("item-name")

# EX:
list_1.remove("cherry")
print(list_1)
