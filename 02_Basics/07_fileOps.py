"""
1. r-> read
2. a->append :
[in existing file write <data> if file not there then it create file]

3. w -> write : 
[if file exist then overwrite the data
if not exist then create the file]

4. 
"""


# @Reading File
# read(value)
# f = open("newfile.txt", "r")
# f = open("newfile.txt", "a")
f = open("newfile.txt", "w")

# print(f.read())
# print(f.readline())
# print("shivam" in f.read())  # True
# f.close()

# for i in f:
#     print(i)


# 1
# @Adding text 
# f.write("\nJay\n")
# f.write("ajay\n")



f.write("abhi")
f.close()