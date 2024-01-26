### TUPLES ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = ("RollerSkating", "painting", "reading", "running", "coocking", "going to the gym")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple.count("running"))
print(my_tuple.index("reading"))

# my_tuple[1] = "programming"   TypeError: 'tuple' object does not support item assignment

print(my_tuple)

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[1] = "programming" 
print(my_tuple)
my_tuple.insert(1, "swimming")

