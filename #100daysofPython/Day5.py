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
rover = Dog('
