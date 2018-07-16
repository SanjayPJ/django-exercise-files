
name = "sanjay pj"

def greet():
    name = "Sam"

    def hello():
        print("Hello " , name)

    hello()

greet()

print(name)

def demo():
    global name
    print(name)

demo()
