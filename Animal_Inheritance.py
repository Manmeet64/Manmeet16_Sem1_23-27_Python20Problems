'''
Create a base class called “Animal” and two subclasses, “Dog” and “Cat.” Add
methods and attributes specific to each subclass.
'''
# Base class for animals
class Animal:

    # Constructor to initialize name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Placeholder methods to be overridden in subclasses
    def make_sound(self):
        pass  # Will be implemented in subclasses

    def behaviour(self):
        pass  # Will be implemented in subclasses

# Class for dogs, inheriting from Animal
class Dog(Animal):

    # Constructor to initialize name, age, and breed
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call the parent class constructor
        self.breed = breed

    # Method to return the sound a dog makes
    def make_sound(self):
        return "Woof!"

    # Method to return a dog's behavior
    def behaviour(self):
        return f"{self.name} is wagging its tail."

# Class for cats, inheriting from Animal
class Cat(Animal):

    # Constructor to initialize name, age, and color
    def __init__(self, name, age, color):
        super().__init__(name, age)  # Call the parent class constructor
        self.color = color

    # Method to return the sound a cat makes
    def make_sound(self):
        return "Meow!"

    # Method to return a cat's behavior
    def behaviour(self):
        return f"{self.name} is purring."

# Main function to demonstrate animal object creation and behavior
def main():
    dog = Dog("Bruno", 3, "Golden Retriever")
    cat = Cat("Chippy", 2, "ginger")

    # Print animal information
    print(f"{dog.name} is a {dog.age}-year-old {dog.breed}.")
    print(f"{cat.name} is a {cat.age}-year-old {cat.color} cat.")

    # Print animal sounds and behaviors
    print(f"{dog.name} goes {dog.make_sound()}")
    print(f"{cat.name} goes {cat.make_sound()}")
    print(dog.behaviour())
    print(cat.behaviour())

# Call the main function if the script is executed directly
if __name__ == "__main__":
    main()
