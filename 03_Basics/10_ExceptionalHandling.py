"""
url = input("Enter file location : ")
try:
    f = open(url, "r")
    print(f.read())
except:
    print("Error >> Entered wrong file location ")
"""

"""
url = input("Enter file location : ")
try:
    f = open(url, "r")
    print(f.read())
except FileNotFoundError:
    print("Error >> Entered wrong file location ")
"""

# JAb <FileNotFoundError> error nahi ayega then
# print hoga --> print("Error >> Entered wrong file location ")

url = input("Enter file location : ")
try:
    f = open(url, "r")
    print(f.read())
except Exception as e:
    print("Error >>", e)
