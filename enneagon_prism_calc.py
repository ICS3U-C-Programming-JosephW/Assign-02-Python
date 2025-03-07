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
    print(
        """Hello user! This is a program designed to 
calculate the volume, surface area, lateral surface area, 
and base area of an enneagonal prism!\n"""
    )

    # Use util function to get the user's choice for calculation.
    calc_choice = util_funcs.init_choice_input()
    
    # Create a base edge prompt.
    base_edge_prompt = "Enter the base edge length."
    # Create a height prompt.
    height_prompt = "Enter the height."

    # Match the calculation choices.
    match calc_choice:
        # Ask for base edge length and height for volume, ...
        case "Volume" | "Surface Area" | "Lateral Surface Area":
            input(base_edge_prompt)
            input(height_prompt)
        case "Base Area":
            input(base_edge_prompt)
    


    
    # Filler text.
    print("...")

# Checks if this is the main file being scanned.
if __name__ == "__main__":
    # Runs the main function.
    main()
