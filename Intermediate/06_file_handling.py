### FILE HANDLING ###

import os

# .txt file
txt_file = open("Intermediate/file.txt", "w+") # r+ === Read & Write
txt_file.write("My name is Rodrigo López Soria \nI work as a Web Developer \nAs of today (28/01/2024) I am learning Python \nI am 30 years old")
# print(txt_file.read())
# print(txt_file.read(10))
# print(txt_file.readline())
# print(txt_file.readline())
print(txt_file.readlines())

txt_file.write("\nAlthough I feel like I am still 23 y.o.")

txt_file.close()

os.remove("Intermediate/file.txt")


# .json file

import json

json_file = open("Intermediate/file.json", "w+")

json_test = {
    "name":"Rodrigo López Soria", 
    "occupation":"Web Developer", 
    "age":"30",
    "website": "https://rodrigolopez.netlify.app/",
    "stack": ["JavaScript", "Node", "React", "HTML", "CSS", "Express", "Github", "MongoDB", "Docker", "Terraform", "Ansible", "Prometheus", "Grafana"]
    }

json.dump(json_test, json_file, indent= 2)

json_file.close() # If you don't close it, you can't read it

with open("Intermediate/file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])


# .csv file

import csv

json_test = {
    "name":"Rodrigo López Soria", 
    "occupation":"Web Developer", 
    "age":"30",
    "website": "https://rodrigolopez.netlify.app/",
    "stack": ["JavaScript", "Node", "React", "HTML", "CSS", "Express", "Github", "MongoDB", "Docker", "Terraform", "Ansible", "Prometheus", "Grafana"]
    }

csv_file = open("Intermediate/file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "occupation", "age", "website", "stack"])
csv_writer.writerow(["Rodrigo López Soria", "Web Developer", "30", "https://rodrigolopez.netlify.app/", "Python"])
csv_writer.writerow(["Laura Smith", "DevOps engineer", "", "", "Terraform"])

csv_file.close()
# .xlsx file

# import xlrd # Must be installed 


# .xml file

import xml

