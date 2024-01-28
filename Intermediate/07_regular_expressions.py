### REGULAR EXPRESSIONS ###

import re

my_string = "This is lesson number 7: Lesson Regular Expressions"
my_other_string = "This is not lesson number 6: File Handling"

match = re.match("This is lesson", my_string, re.I)
print(match)

start, end = match.span()
print("hello", my_string[start:end])


print(re.match("This is lesson", my_other_string))

if match != None:
    print(match)
    start, end = match.span()
    print(my_string[start:end])

print(re.match("Regular Expressions", my_string))


# search

search = re.search("lesson", my_string, re.I)
print("the search", search)
start, end = search.span()
print(my_string[start:end])


# findall

findall = re.findall("lesson", my_string, re.I)
print(findall)

# split

print(re.split("\n", my_string))

# sub

re.sub("Regular", "regular", my_string)
print(re.sub("[l|L]esson", "LESSON", my_string, re.I))
re.sub("Regular Expressions", "RegEx", my_string)

# Patterns 

pattern = r"[lL]esson|[eE]xpressions"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))

email = "rodrigolopezsoria@gmail.com"
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

print(re.match(email_pattern, email))
print(re.search(email_pattern, email))
print(re.findall(email_pattern, email))

email = "rodrigolopezsoria@gmailcom"
print(re.match(email_pattern, email))


# https://regex101.com/
