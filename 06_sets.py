### SETS ###

my_set= set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # initally it's read as DICT


my_other_set = {"Boletus", "Tartufo", "French Fries"}
print(type(my_other_set)) # Now it's read as SET

my_other_set.add("Brussel Sprouts")
print(my_other_set) # A set is NOT an ordered structure

my_other_set.add("Brussel Sprouts") 
print(my_other_set) # A set doesn't admit repeated values

# To check if an element exists in a set

print("Boletus" in my_other_set)
print("Boletos" in my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) 

my_set = { "Olives", "Wine", "Pizza"}
my_list = list(my_set)

my_other_set = { "Spinacs", "Blueberries", "Red pepper"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union({"Chickpeas", "Lentils"}))
print(my_new_set) # It doesn't save the union unless you save it inside a new variable

print(my_other_set.difference({"Blueberries"}))
