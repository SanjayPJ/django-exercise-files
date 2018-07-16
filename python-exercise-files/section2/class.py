
class Sample_dog():
    species = "mamal"
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

sample_dog0 = Sample_dog("eg0_breed", "saddy");
sample_dog1 = Sample_dog("eg1_breed", "jager")

print(sample_dog0.breed, sample_dog0.name)
print(sample_dog1.breed, sample_dog0.name)

print(sample_dog0.species, sample_dog1.species)


class Calculate_circle():

    pi = 3.14;
    def __init__(self, radius = 5):
        self.radius = radius;
    def area(self):
        return self.radius * self.radius * Calculate_circle.pi
    def set_rad(self, new_r):
        self.radius = new_r

my_circle = Calculate_circle();

print(my_circle.area())

my_circle.set_rad(45);

print(my_circle.area())


class Animal():

    def __init__(self):
        print("Animal class created")

    def __str__(self):
        return "this is a dog"

    def __len__(self):
        return 1

    def __del__(self):
        print("Animal deleted successfully")

    def whoami(self):
        print("I am an animal")

    def eat(self):
        print("sorry i dont eat self, lol")

animal0 = Animal()
animal0.whoami()
animal0.eat()
print(animal0)
print(len(animal0))


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog class created")

    def bark(self):
        print("yea i can bark")


my_dog0 = Dog();
my_dog0.whoami();
my_dog0.eat();
my_dog0.bark();

del my_dog0
