#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 6, 2025
# This module contains utility functions (helper functions).

# Import the constants module.
import constants

def init_choice_input():
    # Construct an infinite loop.
    while True:
            # Try to get a correct input from the user.
            try:
                # Get what the user wants to calculate for the enneagonal prism.
                target_calculation = input("What do you want to calculate out of the mentioned properties?\n")
                
                # Checks if the user did not input a valid choice.
                if str.title(target_calculation) not in constants.ACCEPTED_CHOICES:
                
                    # Trigger a value error stating the user did not pick a valid choice.
                    raise ValueError("Please pick a valid choice.")
                else:
                    # Print out a string indicating that the user chose correctly.
                    print(f"Alright! Remember, you chose {str.title(target_calculation)}.")
                    
                    # Return the value to use it in future calculations.
                    return target_calculation
            except ValueError as error_msg:
                 print(error_msg)

def interpolate_colours():
     pass