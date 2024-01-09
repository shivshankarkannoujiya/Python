# slicing
"""
var_name[startIndex:endIndex]
startIndex : included
endIndex : excluded
"""

name = "Abhishek"
# print(name[1:4])  # bhi

"""
startIndex : b {included}
endIndex : s {excluded}
so,
output ==> [bhi]
"""


# 1
# @string Formatting
# @print in upperCase
firstName = "abhishek"
# print(firstName.upper())

# @print in lowerCase
lastName = "KANNOUJIYA"
# print(lastName.lower())


# 2
# @print each word seprately :
# seprater = space " "
# .split(seprater<>spcae , comma etc)
myMsg = "My name is Abhi"
# print(myMsg.split(" "))

# output : ['My', 'name', 'is', 'Abhi']

# 3
# @printing lenght of string
# len(str_name)
# print(len(myMsg))

# 4
# @printing the length of words
"""
var_name.split(" ") : getting list
then, we can find length of list easily and get the count of words in a string

"""
# print(len(myMsg.split(" ")))

# 5
# @concatenate 2 strings

var1 = "Abhi"
var2 = "Kumar"

varConcatenated = var1 + " " + var2
# print(varConcatenated)

# 6
# @printing string multiple times
# print(var1 * 3)


# 7
# @Formatting
# .format(val1,val2,...)

subject = "Mathematics"
marks = 90

# method-1
formattedString = "I have got Marks : {}  in subject :  {} ".format(marks, subject)
# print(formattedString)

# method-2
formattedString2 = f"I have got Marks : {marks} in Subject : {subject}"
# print(formattedString2)


# 8
# @printing \ with string
var3 = "Abhi \\ Kumar"
# print(var3)  # [Abhi \ Kumar]

# @printing \n in a string
var4 = "Abhi \\n Kannouujiya"
# print(var4)

# @removing single char : \b

var5 = "Spider\b man"
# print(var5) # Remove : r

# @Overwrite back string with forward strings : \r
var6 = "Rock \r Joor"
# print(var6) # Joor
