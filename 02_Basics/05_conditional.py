a = 10
b = 20

"""
if a > b:
    print("a is greater")
elif a == b:
    print("both are equal")
else:
    print("b is greater")

"""

# @Shortcut
print("a is greater") if a > b else print("b is gretaer")


if a > b:
    print("a is greater")
else:
    if a == b:
        print("both are equal")
    else:
        print("b is greater")

# @Shortcut
print("a is greater") if a > b else print("both equal") if a == b else print(
    "b is greater than a"
)
