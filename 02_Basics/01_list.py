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

# 7
# ===== @deletefromlist <remove> =====
# if duplicate : Remove the first Occurence
# list.remove("item-name")

# EX:
# list_1.remove("cherry")
# print(list_1)


# 8
# @using-pop()
# list.pop(index)
# We can save the deleted item in a Variable


# list_1 = ["apple", "Mango", "Banana", "cherry"]
# EX:

# deletedItem = list_1.pop(2)
# print("list after deletion : ", list_1)
# print("Deleted_item : ", deletedItem)


# 9
# @Delete from Memory <del>
# del list[index]
# del list_name : delete whole list from memory

# del list_1[2]
# print(list_1)

# del list_1
# print(list_1)
# NameError: name 'list_1' is not defined.
# Because list_1 deleted form memory


# @Sorting
# list_Name.sort()

# EX:
# list_1.sort()
# print(list_1)

# @also give parameter : reverse = True
# list_1.sort(reverse=True)
# print(list_1)


# @Creating copy of list
# var_name[to store copy] = list.copy()
# copies only value does not memory address

Copy_list = list_1.copy()
# print(list_1)
# print(Copy_list)
# print(list_1 is Copy_list)  # False

# @copy value as well as memory Address
Copy_list2 = list_1
# print(list_1)
# print(Copy_list2)
# print(Copy_list2 is list_1)


# @Concatenating 2 lists
l1 = ["mango", "grapes"]
l2 = ["orange", "banana"]
combined_list = l1 + l2
# print(combined_list)  # ['mango', 'grapes', 'orange', 'banana']


# @Printing length of list > len()
length_of_list_1 = len(list_1)
print("Length : ", length_of_list_1)
