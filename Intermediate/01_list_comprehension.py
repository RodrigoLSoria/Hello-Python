### LIST COMPREHENSION ###

my_stack_list = ["JavaScript", "Node", "React", "HTML", "CSS", "Express", "Github", "MongoDB", "Docker", "Terraform", "Ansible", "Prometheus", "Grafana"]

my_list = [ i for i in my_stack_list]
print(my_list)

my_list = [ i for i in range(40)]
print(my_list)

my_list = [ i * i for i in range(40)]
print(my_list)

def sum_five (number):
    return number + 5

my_list = [ sum_five(i) for i in range(40)]
print(my_list)

my_list= range(30)
print(list(my_list))
