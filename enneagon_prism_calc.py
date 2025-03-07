#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 6, 2025
"""
This program allows the user to calculate the volume,
surface area, lateral surface area, and base area of
an enneagonal prism by asking them for the base edge length
and height.
"""

# Import the constants and utility functions modules into this file.
import constants
import util_funcs


# Runs the main function thread.
def main():
    # Greet the user.
    print(
        '''Hello user! This is a program designed to 
calculate the volume, surface area, lateral surface area, 
and base area of an enneagonal prism!\n'''
    )

    # Get and check the user's choice for calculation using a utility function.
    calc_choice = util_funcs.init_choice_input()

    # Get and check the user's choice for units using a utility function.
    unit = util_funcs.check_unit_options()

    # Get the base edge length from the user.
    base_len = float(input("Enter the base edge length."))

    # Match the calculation choices for getting height.
    match calc_choice:
        # Ask for height only with volume, surface area, and lateral surface area, not base area.
        case "Volume" | "Surface Area" | "Lateral Surface Area":
            # Get height from user.
            height = float(input("Enter the height."))

    # Get the amount of decimal places the user wants to round to.
    places_to_round = int(
        input("How many decimal places would you like to round the answer to?")
    )

    # Calculate the desired result, including units and round.
    result = util_funcs.calculate_enneaprism(
        calc_choice, base_len, height, unit, places_to_round
    )

    # Display the result to the user.
    print(f"The {calc_choice} of your enneagonal prism is: {result}")


# Checks if this is the main file being scanned.
if __name__ == "__main__":
    # Runs the main function.
    main()
