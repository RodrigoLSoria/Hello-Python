### FUNCTIONS ###

def my_function ():
    print("I am a master of Python")

my_function ()

def sum_two_values (first_value, second_value):
    print(first_value + second_value)

sum_two_values(3456, 23456)
sum_two_values(1,2)
sum_two_values("2", "3")

# just like in javascript, you have to return the function if you want to keep the retrieved data

def sum_two_values (first_value, second_value):
    my_sum =  first_value + second_value
    return my_sum

my_result = sum_two_values(1, 24)
print(my_result)

def print_full_name (name, surname):
    print(f"{name} {surname}")

print_full_name(name = "Rodrigo", surname = "López Soria")

def print_default_full_name (name = "Rodrigo", surname = "López Soria", nickname = "Rod"):
    print(f"{name} {surname}, alias {nickname}")

print_default_full_name()

def print_texts (*text):
    print(text)

print_texts("Hola, I want to travel the world and work in amazing projects", "I am most passionate about enviromentalism")

