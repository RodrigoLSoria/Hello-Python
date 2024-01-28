### LOOPS ###

# while

my_condition = 0

while my_condition < 10 : 
    print("Hey you! this is my_condition value in this iteration:", my_condition)
    my_condition += 1
# elif my_condition == 10 :
# print("my_condition is == to 10")
else:
    print("my_condition is equal to, or greater than 10 ")

print("the condition no longer applies")

while my_condition < 20 :
    my_condition += 2
    if my_condition == 16 : 
        print("my_condition is == to 16")

# For
        
my_list = [30, 13, 9, 6, 1993, 35, 24]

for element in my_list:
    print(element)



my_tuple = ("RollerSkating", "painting", "reading", "running", "coocking", "going to the gym")

for element in my_tuple:
    print(element)



my_other_dictionary = {
    "name":"Rodrigo López Soria", 
    "occupation":"Web Developer", 
    "age":"30",
    "stack": {"JavaScript", "Node", "React", "HTML", "CSS", "Express", "Github", "MongoDB", "Docker", "Terraform", "Ansible", "Prometheus", "Grafana"}
    }

for element in my_other_dictionary:
    print(element)
    if element == "age":
        break

else:
    print("the dictionary's loop has finished")

my_set = { "Olives", "Wine", "Pizza"}

for element in my_set:
    print(element)
