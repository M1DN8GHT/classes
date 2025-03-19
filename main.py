class Animal:
    form_of_life = "carbon-based"
    num_animals = 0

    def __init__(self, name, species, num_legs=0, num_eyes=0):
        self.name = name
        self.species= species
        self.num_legs = num_legs
        self.num_eyes = num_eyes
        Animal.num_animals += 1


    def print_info(self):
        print(f"{self.name} is a {self.species} with {self.num_legs} legs and {self.num_eyes} eyes.")

    def rename(self, new_name):
        self.name = new_name



dog = Animal("Rex", "Wolf", num_legs=4, num_eyes=2)
cat = Animal("Mittens", "Cat", num_legs=4, num_eyes=2)
fish = Animal("Nemo", "Fish", num_legs=0, num_eyes=2)
print(Animal.num_animals)
