### EXCEPTION HANDLING ###

number_one = 10
number_three = 13
# number_three = "2024"

try:
   print(number_one + number_three)
   print("No errors")
except:
   print("There's an error")

# Try, Except, Else, Finally
   

number_four = 10
number_five = 13
number_five = "2024"

try:
   print(number_four + number_five)
   print("No errors")
# except ValueError:
#    print("There is a Value Error")
# except TypeError:
#    print("There is a Type Error")
except ValueError as error:
   print(error)
except TypeError as error:
   print(error)
except Exception as exception:
   print(exception)
except:
   print("There's an error")
else: #Optional
   # else depends on the condition to execute
   print("Execution continues with no errors")
finally: #Optional
   # Finally will ALWAYS execute
   print("Execution continues")
