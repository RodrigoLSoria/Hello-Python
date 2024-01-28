### HIGHER ORDER FUNCTIONS ###

def sum_one (value):
    return value + 1

def sum_five (value):
    return value + 5

def sum_two_values_plus_one (first_value, second_value, f):
    return f(first_value + second_value)

print(sum_two_values_plus_one(5, 2, sum_one))
print(sum_two_values_plus_one(5, 2, sum_five))


### Closures ###

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))

### BUILT-IN HIGHER ORDER FUNCTIONS ###

numbers = [ 1, 10, 23, 13, 93, 2024]

# MAP

def multiply_values (value):
    return value * 2


print(list(map(multiply_values, numbers)))
print(list(map(lambda value: value * 3, numbers)))

# FILTER

def filter_greater_than_10(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_10, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# REDUCE

from functools import reduce

def sum_two_values(first_value, second_value):
    print( "El first value",first_value)
    print(second_value)
    return  first_value + second_value

print(reduce(sum_two_values, numbers))