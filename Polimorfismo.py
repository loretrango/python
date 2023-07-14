class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Polymorphic function
def animal_sounds(animal):
    print(animal.make_sound())

# Create instances of different animals
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

# Call the polymorphic function with different animals
animal_sounds(dog)  # Output: Woof!
animal_sounds(cat)  # Output: Meow!
animal_sounds(cow)  # Output: Moo!
print(cow.make_sound())
