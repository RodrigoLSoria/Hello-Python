### MODULES ###

# my_function() #NameError: name 'my_function' is not defined

import module

module.my_function(1,2,3)

module.printValue("Hola Python!")   


# By importing the functions as follow you dont need to use the above method
from module import my_function

my_function(4,5,6)

import math

print(math.pi)
print(math.pow(2,8))

import random

print(random.random())


from math import pi as PI_VALUE

print(PI_VALUE)
