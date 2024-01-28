# Strings

my_string= "Hey I am a string"
my_other_string= "Hey I am the other string"

print(len(my_string))
print(len(my_other_string))
print(my_other_string + " " + my_string)

# Strings with line break
my_line_break_string= "Hello, I am so excited about \n learning Python, can't wait to get my hands on a real project with this amazing technology"
print(my_line_break_string)

# String with Tab
my_tab_string= "\tThis is my tab string"
print(my_tab_string)

# String with Scape
my_scape_string= "\\tThis is my tab string"
print(my_scape_string)

# Formatting
name, surname, age, location = "Rodrigo", "Lopez Soria", 30, "Madrid"

print("My name is {} {}, I am {} y.o. and living in {}".format(name, surname, age, location))
print("My name is %s %s, I am %s y.o. and living in %s" %(name, surname, age, location)) 
print(f"My name is {name} {surname}, I am {age} y.o. and living in {location}")

# Unpacking characters
hobby= "rollerskating"
 # a,b = hobby # This will result in an error as it needs the same amount of characters as in hobby's value

#the correct way would be as follows:
a,b,c,d,e,f,g,h,i,j,k,l,m = hobby
print(a)
print(b)
print(c)

 # Slicing
hobby_slice = hobby[1:6]
print(hobby_slice)

# Reversing
reversed_hobby= hobby[:: -1]
print(reversed_hobby)

# Functions
print(hobby.capitalize())
print(hobby.casefold())
print(hobby.count("l"))
print(hobby.find("7"))
print(hobby.isnumeric())
print(hobby.upper())
print(hobby.lower())
print(hobby.lower().islower())
