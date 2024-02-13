### Type Hints ###
my_python_variable = "I am the snake variable"
print(my_python_variable)
print(type(my_python_variable))

# Python uses dynamic typing, therefore allowing for variables to easily change their type

my_python_variable = 5
print(my_python_variable)
print(type(my_python_variable))

# Even typing the variable you won't force it to stay that way = 

my_typed_variable: int = "Hello there!"
print(my_typed_variable)
print(type(my_typed_variable))

my_typed_variable=5
print(my_typed_variable)
print(type(my_typed_variable))

#However, type hints will allow fastAPI to add an extra leyer of securiy to the code

my_typed_variable: int = "Hello there!"
my_typed_variable.__abs__
my_typed_variable.bit_length

my_typed_variable: str = "Hello"
my_typed_variable.capitalize
my_typed_variable.casefold
