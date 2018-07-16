
#if statement
if True:
    print("yea i got it")

#if else
if False:
    print('not gonna print')
else:
    print('gonna print yaar')

#else if
if False:
    print("not gonna print")
elif True:
    print("its gonne print")

# for loop
for i in range(10):
    print(i)

#print dictionary

my_dictionary = {"name":"sanjay", "age":18}

for i in my_dictionary:
    print(i)
    print(my_dictionary[i])

#print pairs

my_pairs = [(1, 2), (6, 3)]

for (num1, num2) in my_pairs:
    print(num1)
    print(num2)

# while loop

i = 0;
while(i <= 9):
    print("Hello World")
    i+=1

even_numbers = list(range(2,45,2))

print(even_numbers)


# fuctions


def hack_the_world():
    print("hacked")

hack_the_world()


def hack_the_world0():
    """this is gonna be the doc string"""
    print("after the docstring you have been hacked")

#hover it to see the docstring

hack_the_world0()

def return_something():
    return "hello World"

print(return_something())


#lambda

my_list0 = [1,2,3,4,5,6]

even_num_from_list = list(filter(lambda num:num%2==0 , my_list0))

print(even_num_from_list)
