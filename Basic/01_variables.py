# In python, variables can have upper case characters, however convention suggest to not use them and use 
# snake case
my_python_variable = "I am the snake variable"
print(my_python_variable)

my_int_variable = 11
print(my_int_variable)

my_boolean_variable = False
print(my_boolean_variable)

print("my python variable:", my_python_variable, ", my int variable:", my_int_variable, ", my boolean variable:", my_boolean_variable)


# Some System's Functions: 

# now we use str() function to convert numbers to string
my_int_to_str_variable = str(my_int_variable)
print("my int to str variable:", my_int_to_str_variable)

# length function
print(len(my_python_variable))

#One line variables
name, surname, alias, age = "Rodrigo", "Lopez Soria", "Rodri", 30

# Inputs, with them you can overwrite variables
name= input("What is your name?")
age= input("How old are you?")

# once we input the data, we can check the new value with the following prints = 

print("my name is", name)
print("I am", age)

# There is no Const in Python, so if one needs a constant variable, one should indicate it as follows = 
CONST_NAME = "Rodrigo"