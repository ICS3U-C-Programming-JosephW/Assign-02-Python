#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 6, 2025
# This module contains utility functions (helper functions).

# Import the constants and math modules.
import constants
import math

# Define a function to manage user choice input.
def init_choice_input():
    # Construct an infinite loop.
    while True:
        # Try to get a correct input from the user.
        try:
            # Get what the user wants to calculate for the enneagonal prism.
            target_calculation = input(
                f"""{constants.LIGHT_CYAN}What do you want to calculate? Again, choices are: 
volume, surface area, lateral surface area, or base area. 
Enter only one of these.{constants.WHITE}\n"""
            )
            # Checks if the user did not input a valid choice with lowercase conversion.
            if str.lower(target_calculation) not in constants.ACCEPTED_CHOICES:
                # Raise a red ValueError stating the user did not pick a valid choice.
                raise ValueError(
                    f"""\n{constants.LIGHT_RED}Please pick volume, surface area,
lateral surface area, or base area.{constants.WHITE}\n"""
                )
            # Otherwise, checks if the user did input a valid choice.
            else:
                # Print out a light purple string indicating that the user chose correctly.
                print(f"\n{constants.LIGHT_PURPLE}Alright!{constants.WHITE}\n")

                # Return the lowercase version of string to use in display.
                return str.lower(target_calculation)
        # Get the raised ValueError message and print it as an exception.
        except ValueError as error_msg:
            print(error_msg)


def check_unit_options():
    # Construct an infinite loop.
    while True:
        # Try to get a valid unit from the user.
        try:
            # Get the unit from the user.
            unit = input(
                f"""{constants.LIGHT_PURPLE}Enter what units you want the answer to be in.
Choices are: mm, cm, in, or ft.{constants.WHITE}\n"""
            )
            # Checks if the user did not input a valid unit choice.
            if str.lower(unit) not in constants.ACCEPTED_UNITS:
                # Raise a red ValueError stating the user did not pick a valid choice.
                raise ValueError(
                    f"\n{constants.LIGHT_RED}Please pick mm, cm, in, or ft.{constants.WHITE}\n"
                )
            # Otherwise, checks if the user did input a valid unit choice.
            else:
                # Display a proceeding message indicating that the user chose correctly.
                print(f"\n{constants.LIGHT_CYAN}Done!{constants.WHITE}")
                # Return the unit in lowercase.
                return str.lower(unit)
        # Get the raised ValueError message and print it as an exception.
        except ValueError as error_msg:
            print(error_msg)

# Define a function for managing valid number input from the user.
def check_positive_num(display_message, num_type, str_type):
    # Construct an infinite loop.
    while True:
        # Try to create a dynamic input system.
        try:
            """Gets input from a user and converts it to a number type with
            a custom display message.
            """
            any_num = num_type(input(display_message))
            # Checks if number is less than or equal to 0 and is a float.
            if any_num <= 0 and str_type == "float":
                # Raise a red ValueError indicating the user did not pick a whole number.
                raise ValueError(
                    f"""\n{constants.LIGHT_RED}Please pick a positive 
and non-zero value.{constants.WHITE}"""
                )
            # Checks if the number is less than 0 and is an integer.
            elif any_num < 0 and str_type == "int":
                # Raise a red ValueError indicating the user did not pick a positive value.
                raise ValueError(
                    f"\n{constants.LIGHT_RED}Please pick a positive value.{constants.WHITE}"
                )
            # Checks if the user does not do any of the above things.
            else:
                # Displays a green text to proceed.
                print(f"\n{constants.LIGHT_GREEN}Accepted.{constants.WHITE}")
                # Return the number.
                return any_num
        # Get the raised ValueError message and print it as an exception.
        except ValueError as error_msg:
            print(error_msg)

# Define a function to calculate the user's desired result for an enneagonal prism.
def calculate_enneaprism(choice, base_len, height, unit, round_num):
    # Match the choice with the following cases.
    match choice:
        # The volume case.
        case "volume":
            # Calculate the formula for volume in a variable.
            volume = 9 / 4 * (base_len**2) * 1 / math.tan(math.pi / 9) * height
            # Format the result to the desired amount of decimal places with units.
            return f"{volume:.{round_num}f} {unit}^3"

        # The surface area case.
        case "surface area":
            # Calculate the formula for surface area in a variable.
            surface_area = 9 * base_len * height + 9 / 2 * (
                base_len**2
            ) * 1 / math.tan(math.pi / 9)
            # Format the result to the desired amount of decimal places with units.
            return f"{surface_area:.{round_num}f} {unit}^2"

        # The lateral surface area case.
        case "lateral surface area":
            # Calculate the formula for lateral surface area in a variable.
            lateral_surface_area = 9 * base_len * height
            # Format the result to the desired amount of decimal places with units.
            return f"{lateral_surface_area:.{round_num}f} {unit}^2"

        # The base area case.
        case "base area":
            # Calculate the formula for base area in a variable.
            base_area = 9 / 4 * (base_len**2) * 1 / math.tan(math.pi / 9)
            # Format the result to the desired amount of decimal places with units.
            return f"{base_area:.{round_num}f} {unit}^2"
