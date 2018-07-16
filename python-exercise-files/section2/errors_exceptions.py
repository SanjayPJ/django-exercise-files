
try:
    f = open("simple.txt", "r")
    f.write("test write to simple text!")
except IOError:
    print("Error: IOError")
finally:
    print("I always work no matter what")

print("hello word");
