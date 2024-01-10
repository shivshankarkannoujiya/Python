dict_ = {}
# print(type(dict_)) #<class 'dict'>


# Dictionary
"""
1. Key:value pair
2. Does not contain duplicate value 

"""

dict_1 = {"name": "Abhi", "age": 20, "is Male": True, "name": "shivam"}
# print(type(dict_1))
# print(dict_1)


# 1
dict_2 = {"name": ["Abhi", "shivam"], "age": 21}

# 2
# @Accessing Value
# dict_name['key']
# dict_name.get('key)


# Ex:
# print(dict_2['age'])
# print(dict_2.get('name'))

# 3
# @printing All keys
# print(dict_2.keys())

# 4
# @printing single name
# print(type(dict_2["name"]))

# print(dict_2["name"][0])

# 5
# @Adding Values

# dict_2["location"] = "Delhi"
# print(dict_2)

# 6
# @update

dict_2.update({"location": "delhi"})
# print(dict_2)

# 7
# @ Deleting Values
# dict_2.pop('age')
# print(dict_2)


# 8
# @popitem()
# Delete the ends value

# dict_2.popitem()
# print(dict_2)

# 9
# @del value

# del dict_2["age"]
# print(dict_2)

# 10
# @.clear()

# dict_2.clear()
# print(dict_2)

# 11
# @copy

# dict3 = dict_2.copy()
# print(dict3)


# @Nested Dictionary

d1 = {"Abhi": {"name": "shivam", "age": 20}, "happy": {"name": "ashish", "age": 22}}
print(d1)