# @while

"""
i = 0
while i < 10:
    if i == 4:
        break
    print(i)
    i += 1

"""


# @continue
"""
i = 0
while i < 10:
    i += 1
    if i == 4:
        # continue
        pass
    print(i)
else:
    print("Loop ended.....")

"""

# @range
# print(range(10))
# range(sValue,eValue,stepValue)

# @for-loop
"""
for i in range(5):
    print(i)
"""

"""
for i in range(2,10,2):
    print(i)
"""

# 1
# @iterate on list
"""
l1 = ["apple","banana","chiku","cherry"]
for i in l1:
    print(i)
"""

# 2
"""
l1 = ["apple", "banana", "cherry"]
price = ["40rs", "50rs", "100rs"]

for i in l1:
    for j in price:
        print(i, " : ", j)
"""

# 3
# @iterate on Dictionary
# only keys
# key value both
# keys ke through valuue

d1 = {"name": "abhi", "age": 20, "location": "Noida"}

# Accessing Keys
for i in d1.keys():
    # print(i) # keys
    print(d1[i])  # value

# Method-2
for keys, values in d1.items():
    print(keys, " : ", values)
