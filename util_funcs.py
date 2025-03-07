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
                "What do you want to calculate out of the mentioned properties?\n"
            )
            # Checks if the user did not input a valid choice using titled format.
            if str.title(target_calculation) not in constants.ACCEPTED_CHOICES:
                # Raise a red ValueError stating the user did not pick a valid choice.
                raise ValueError(f"{constants.RED}Please pick a valid choice.{constants.WHITE}")
            else:
                # Print out a green string indicating that the user chose correctly.
                print(f"{constants.GREEN}Alright!{constants.WHITE}")

                # Return the value to use it in future calculations.
                return str.title(target_calculation)
        # Get the raised ValueError message and print it as an exception.
        except ValueError as error_msg:
            print(error_msg)

def generate_given_prompts(input_text):
    prompt1 = "Enter the base edge length."
    prompt2 = "Enter the height."

    match input_text:
        case "Volume" | "Surface Area" | "Lateral Surface Area":
            input(prompt1)
            input(prompt2)
        case "Base Area":
            input(prompt1)

def calculate_enneaprism(input_text, base_len, height, round_num):
    
    match input_text:
        case "Volume":
            return (9/4 * base_len^2 * 1/math.tan(math.radians(20)) * height)
        case "Surface Area":
            return 

def interpolate_colors():
    pass
