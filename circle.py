"""
description: Calculate the area and circumference of a circle from its radius
Steps:
Create a file named circle.py in all lowercase.
Add a docstring to the top of the file containing a description and major tasks of the program (see details below).
Import the math module.
Prompt the user to enter the radius of the circle.
Convert the user entered value from a string to an integer.
Calculate the circumference of the circle and save as a variable named circumference.
Calculate the area of the circle and save as a variable named area.
Use the print function to display the circumference, area and radius. Use the Python Formatted string literals (also called f-strings for short).
Upload your file to your GitHub account and send me the link.
"""

import math

radius = int(input('Please enter a radius: '))
print(type(radius))

circumference = 2 * math.pi * radius

area = math.pi * radius ** 2
print(f'The circumference is {circumference}, the area is {area} for the radius is {radius}')