#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 6, 2025
"""
This program allows the user to calculate the volume, 
surface area, lateral surface area, and base area of
an enneagonal prism by asking them for the base edge and 
height, or just the base edge.
"""

# Import the utility functions module into this file.
import util_funcs

# Greet the user.
print('''Hello user! This is a program designed to 
calculate the volume, surface area, lateral surface area, 
and base area of an enneagonal prism!\n''')

# Get what the user wants to calculate for the enneagonal prism.
target_calculation = input("What do you want to calculate out of the mentioned properties?\n")

# Use function from the module to validate the user's choice.
util_funcs.validate_property_choice(target_calculation)


