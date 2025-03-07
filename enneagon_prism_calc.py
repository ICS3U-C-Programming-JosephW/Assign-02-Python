#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 6, 2025
"""
This program allows the user to calculate the volume, 
surface area, lateral surface area, and base area of
an enneagonal prism by asking them for the base edge and 
height, or just the base edge.
"""

# Import the utility functions and constants modules into this file.
import constants
import util_funcs

# Runs the main function thread.
def main():
    # Greet the user.
    print('''Hello user! This is a program designed to 
calculate the volume, surface area, lateral surface area, 
and base area of an enneagonal prism!\n''')
    
    # Use util function to construct a user input check.
    util_funcs.init_choice_input()

# Checks if this is the main file that is being run.
if __name__ == "__main__":
    
    # Runs the main function.
    main()

