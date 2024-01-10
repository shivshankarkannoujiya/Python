x = lambda a:a+10
# print(x) # print memory address
# print(x(10))

y = lambda a,b : a+b
# print(y(10,20))

def mult(a):
    return lambda b:a*b
m = mult(2)
print(m(10))