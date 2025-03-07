#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 6, 2025
# This module contains utility functions (helper functions).

def validate_property_choice(input_text):
    # An array of accepted options to choose.
    accepted_array = ["Volume", "Surface Area", "Lateral Surface Area", "Base Area"]

    # Checks if the titled version of the string is in the accepted array.
    if str.title(input_text) in accepted_array:
        print("good")

    # Prompt user to pick something else if this is not true.
    else:
        print("Please pick a valid choice.")