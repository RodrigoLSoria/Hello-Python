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
