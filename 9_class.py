class Dog:
    # Object initialization method (function that is a part of a class = method)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over.")

# Making an instance from a Class
my_dog = Dog('Jasper', 5)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Calling Methods
my_dog.sit()
my_dog.roll_over()

# Creating multiple instances
doug_dog = Dog('Doug', 4)
thein_dog = Dog('Thein', 3)
john_dog = Dog('John', 5)
laura_dog = Dog('Laura', 5)

laura_dog.sit()
doug_dog.roll_over()
thein_dog.sit()
john_dog.roll_over()