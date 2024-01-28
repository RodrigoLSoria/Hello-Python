### CLASSES ###

class Person: # With classes, we dont use snake case but camel case
    def __init__(self, name, surname, alias = "No alias"): # init is a class constructor
        self.full_name = f"{name} {surname} ({alias})"
        self.__name = name # Using __ we make our variable private, line 22 cannot access its value
        self.__surname = surname

    def get_name (self):
        return  self.__name  # to retrieve we need this fucntion, however we cannot alter its value

    def walk (self):
        print(f"{self.full_name} is walking")


my_person = Person("Rodrigo", "López Soria")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Pepito", "Pérez", "El Malo")
print(my_other_person.full_name)

my_other_person.full_name = 100
print(my_other_person.full_name)
# print(my_other_person.name)
print(my_other_person.get_name())