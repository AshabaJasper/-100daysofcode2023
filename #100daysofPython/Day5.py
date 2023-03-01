class Dog:
    # class variable
    species = 'mammal'

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def bark(self):
        print('Woof!')

    # instance method
    def describe(self):
        print(f'{self.name} is a {self.species} that is {self.age} years old.')

# create instances of Dog
fido = Dog('Fido', 3)
rover = Dog('Rover', 5)

# use instance methods
fido.bark()    # prints 'Woof!'
rover.describe()    # prints 'Rover is a mammal that is 5 years old.'
