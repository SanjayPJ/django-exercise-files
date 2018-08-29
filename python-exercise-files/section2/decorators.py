
global00 = "GLOBALE VARIABLE"

def func():
    # global global00
    # global00 = "CHANGED GLOBAL VARIABLE"
    # print(global00)
    # name = 23
    # print(locals())
    # print(globals())
    print(globals()["global00"])

# func()
# print(global00)

def hello(name = "sanjay"):
    return "hello " + name

# print(hello())

greet = hello

# print(greet())

def my_greet(name = "sanjay"):
    print("THE MY_GREET FUNCTION HAS BEEN RUNNING!")

    def inside_greet():
        return "THIS STRING INSIDE INSIDE_GREET"

    def inside_welcome():
        return "THIS STRING INSIDE INSIDE_WELCOME"

    if name == "sanjay":
        return inside_greet
    else:
        return inside_welcome

    print(inside_greet())
    print(inside_welcome())

# my_greet()
# input_def = my_greet()
# input_man = my_greet("someone")

# print(input_def())
# print(input_man())

# inside_greet()
# this is not gonna work


def intro():
    return "sam"

def bar_intro(intro):
    print("Hello " + intro())

# bar_intro(intro)

# ``````````````
# start decorators
# ``````````````


def new_decorator(func):

    def wrap_func():
        print('CODE HERE BEFORE EXCECUTING...')
        func()
        print("FUNC HAS BEEN CALLED")
    
    return wrap_func

def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR")

# func_needs_decorator()

# func_needs_decorator = new_decorator(func_needs_decorator)

# func_needs_decorator()

@new_decorator
def func_needs_decorator00():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR")

func_needs_decorator()
