### DICTIONARIES ###

my_dictionary = dict()
my_other_dictionary = {}

print(type(my_dictionary))
print(type(my_other_dictionary))

my_other_dictionary = {
    "name":"Rodrigo López Soria", 
    "occupation":"Web Developer", 
    "age":"30",
    "stack": {"JavaScript", "Node", "React", "HTML", "CSS", "Express", "Github", "MongoDB", "Docker", "Terraform", "Ansible", "Prometheus", "Grafana"}
    }

print(my_other_dictionary["name"])

my_other_dictionary["name"] = "Pepito Pérez"
print(my_other_dictionary["name"])

# to add new pairs:
my_other_dictionary["languages"] = {"Spanish", "English"}
print(my_other_dictionary)

# to delete:

del my_other_dictionary["age"]
print(my_other_dictionary)

print("Web Developer" in my_other_dictionary) # It lets you search by key, not the value
print("occupation" in my_other_dictionary)

# Functions

print(my_other_dictionary.items())
print(my_other_dictionary.keys())
print(my_other_dictionary.values())

