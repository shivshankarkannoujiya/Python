def greet(name):
    print(name, " Welcome to Defronix !!")


greet("Abhi")


# args
def kids(*args):
    print(args)
    # print(args[1])


# Now we can pass  arguments as much we want
kids("Abhi")


def boy(**k):
    print(k)

boy(l1="Abhi",l2="shivam")