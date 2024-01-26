### LISTS ###
my_list = list()

my_list = [30, 1.83, "Rodrigo", "López Soria"]
my_stack_list = ["JavaScript", "Node", "React", "HTML", "CSS", "Express", "Github", "MongoDB", "Docker", "Terraform", "Ansible", "Prometheus", "Grafana"]

print(my_list)
print(my_list[0])
print(my_stack_list.count(30))
print(my_stack_list + my_list)

my_stack_list.append("Python")
print(my_stack_list)
my_stack_list.insert(1, "Typescript")
print(my_stack_list)

# my_list.clear()

del my_stack_list[6]
print(my_stack_list)


my_list.pop(2)
print(my_list)


my_copied_list = my_stack_list.copy()

print("This is my copied list", my_copied_list)
my_copied_list.reverse()
print(my_copied_list)

my_copied_list.sort()
print(my_copied_list)

print(my_copied_list[2:6][0:1])



