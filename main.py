# parent class
class Animal:
    # Class-level attributes shared by all instances of Animal
    form_of_life = "carbon-based"
    num_animals = 0

    def __init__(self, name, species, num_legs=0, num_eyes=0):
        """
        Initialize an Animal instance with name, species, number of legs, and number of eyes.
        Increment the class-level counter for the number of animals.
        """
        self.name = name
        self.species = species
        self.num_legs = num_legs
        self.num_eyes = num_eyes
        Animal.num_animals += 1

    def print_info(self):
        """
        Print the details of the animal, including its name, species, number of legs, and eyes.
        """
        print(f"{self.name} is a {self.species} with {self.num_legs} legs and {self.num_eyes} eyes.")

    def rename(self, new_name):
        """
        Rename the animal by updating its name attribute.
        """
        self.name = new_name
    
    def speak(self):
        """
        Print a generic animal sound. This method can be overridden by subclasses.
        """
        print(f"{self.name} makes a generic animal sound.")

# child class
class Mammal(Animal):
    def __init__(self, name, species, num_legs=4, num_eyes=2):
        """
        Initialize a Mammal instance with default values for legs and eyes.
        Inherits from the Animal class.
        """
        super().__init__(name, species, num_legs, num_eyes)

    def speak(self):
        """
        Override the speak method to provide a specific sound for mammals.
        """
        print(f"{self.name} barks")

# Create an instance of Mammal and demonstrate its functionality
dog = Mammal("Buddy", "Dog")
dog.print_info()  # Print details of the dog
dog.rename("Max")  # Rename the dog
dog.speak()  # Make the dog speak


fish = Animal("Nemo", "Fish", num_legs=0, num_eyes=0)
