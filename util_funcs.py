#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 6, 2025
# This module contains utility functions (helper functions).

# Import the constants and math modules.
import constants
import math


def init_choice_input():
    # Construct an infinite loop.
    while True:
        # Try to get a correct input from the user.
        try:
            # Get what the user wants to calculate for the enneagonal prism.
            target_calculation = input(
                f'''{constants.LIGHT_CYAN} What do you want to calculate out of the mentioned properties? 
                Choices are: volume, surface area, lateral surface area, or base edge.{constants.WHITE}'''
            )
            # Checks if the user did not input a valid choice using titled format.
            if str.title(target_calculation) not in constants.ACCEPTED_CHOICES:
                # Raise a red ValueError stating the user did not pick a valid choice.
                raise ValueError(
                    f"{constants.RED}Please pick a valid choice.{constants.WHITE}"
                )
            else:
                # Print out a green string indicating that the user chose correctly.
                print(f"{constants.WHITE}{constants.BOLD}Alright!{constants.WHITE}")

                # Return the value to use it in future calculations.
                return str.title(target_calculation)
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
                f'''{constants.LIGHT_PURPLE}Enter what units you want the answer to be in.
                         Choices are: mm, cm, in, or ft (LOWERCASE){constants.WHITE}.'''
            )
            # Checks if the user did not input a valid unit choice.
            if str.title(unit) not in constants.ACCEPTED_UNITS:
                # Raise a red ValueError stating the user did not pick a valid choice.
                raise ValueError(
                    f"{constants.RED}Please pick mm, cm, in, or ft.{constants.WHITE}"
                )
            else:
                # Print out a green string indicating that the user chose correctly.
                print(f"{constants.WHITE}{constants.BOLD}Alright!{constants.WHITE}")
                # Return the unit to use it in future calculations.
                return unit
        # Get the raised ValueError message and print it as an exception.
        except ValueError as error_msg:
            print(error_msg)


def calculate_enneaprism(input_text, base_len, height, unit, round_num):
    match input_text:
        case "Volume":
            return f"{9/4 * base_len**2 * 1/math.tan(math.pi/9) * height} {unit}^3"
        case "Surface Area":
            return f"{9 * base_len * height + 9/2 * base_len**2 * 1/math.tan(math.pi/9)} {unit}^2"
        case "Lateral Surface Area":
            return f"{9 * base_len * height} {unit}^2"
        case "Base Area":
            return f"{9/4 * base_len * 1/math.tan(math.pi/9 * height)} {unit}^2"
