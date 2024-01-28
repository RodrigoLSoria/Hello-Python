### ERROR TYPES ###

# SyntaxError
print "Beware the syntax error" #SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?


# NameError

print(name)  # NameError: name 'name' is not defined


# IndexError

my_stack_list = ["JavaScript", "Node", "React", "HTML", "CSS", "Express", "Github", "MongoDB", "Docker", "Terraform", "Ansible", "Prometheus", "Grafana"]
print(my_stack_list[13]) # IndexError: list index out of range


# ModuleNotFoundError
import maths   # ModuleNotFoundError: No module named 'maths'
import math


# AttributeError
print(math.PI)   # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?


# KeyError
my_dict = {"Name":"Rodrigo", "Surname": "López Soria", "Age":30}
print(my_dict["age"])   # KeyError: 'age'


# TypeError
print(my_stack_list["Name"])   # TypeError: list indices must be integers or slices, not str
 

# ImportError 
from math import pii   # ImportError: cannot import name 'pii' from 'math' (unknown location). Did you mean: 'pi'?


# ValueError
my_int = int("10 años")  # ValueError: invalid literal for int() with base 10: '10 años'
print(type(my_int))


# ZeroDivisionError
print(4/0)   # ZeroDivisionError: division by zero