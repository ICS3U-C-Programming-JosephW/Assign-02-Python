#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 6, 2025
"""
This program allows the user to calculate the volume,
surface area, lateral surface area, and base area of
an enneagonal prism by asking them for the base length 
(edge) and height.
"""

# Import the constants and utility functions modules into this file.
import constants
import util_funcs


# Create the main function.
def main():
    # Greet the user with a light green text.
    print(
        f"""\n{constants.LIGHT_GREEN}Hello, user! This is a program designed to 
calculate the volume, surface area, lateral surface area, 
and base area of an enneagonal prism!{constants.WHITE}\n"""
    )

    # Get and check the user's choice for calculation using a utility function.
    calc_choice = util_funcs.init_choice_input()

    # Get and check the user's choice for units using a utility function.
    unit = util_funcs.check_unit_options()

    # Get the base edge length from the user.
    base_len = util_funcs.check_positive_num(
        f"""\n{constants.LIGHT_PURPLE}Enter the base edge length.{constants.WHITE}\n""",
        float,
        "float",
    )

    # Match the calculation choices for getting height.
    match calc_choice:
        # Ask for height only with volume, surface area, and lateral surface area.
        case "volume" | "surface area" | "lateral surface area":
            # Get height from user.
            height = util_funcs.check_positive_num(
                f"""{constants.LIGHT_YELLOW}
Enter the height of the enneagonal prism.{constants.WHITE}\n""",
                float,
                "float",
            )
        # Height is not needed for base area, so give it a placeholder value.
        case "base area":
            # Set height to 0.
            height = 0

    # Get the amount of decimal places the user wants to round to.
    places_to_round = util_funcs.check_positive_num(
        f"""\n{constants.LIGHT_BLUE}How many decimal places would 
you like to round the answer to?{constants.WHITE}\n""",
        int,
        "int",
    )

    # Calculate the desired result, including units and round.
    result = util_funcs.calculate_enneaprism(
        calc_choice, base_len, height, unit, places_to_round
    )

    # Display the result to the user.
    print(
        f"""\n{constants.DARK_GRAY}The {calc_choice} of your enneagonal prism is: 
{result}{constants.WHITE}\n"""
    )


# Checks if this is the main file being scanned.
if __name__ == "__main__":
    # Runs the main function.
    main()
