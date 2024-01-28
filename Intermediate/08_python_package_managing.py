### PYTHON PACKAGE MANAGING ###

# PIP https://pypi.org

import numpy

print(numpy.version.version)

numpy_array = numpy.array([10,13,93,2024])
print(type(numpy_array))

print(numpy_array * 2)

import pandas #pip install pandas

import requests # pip install requests

response = requests.get("https://greenlet.netlify.app/postDetails/659f0a925b437d927caa7ce9")
print(response)
print(response.json(f))
print(response.status_code)
