#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Oct 15, 2023
# This program will ask the user
# for their age and I will tell them
# if they can date my granddaughter
# with a try catch
import random


def main():
    # Get the user age as a string and display a message
    print("This program will ask the user for their age and I will tell them")
    print("if they can date my granddaughter.")
    user_age_as_string = input("Please enter your age: ")

    # Catch if the user input something wrong
    try:
        # Convert user age as a string to int
        user_guess_as_int = int(user_age_as_string)

        # Check if the user guess as int meets my requirements
        if (user_guess_as_int > 25 and user_guess_as_int < 40):
            # Display if the user can date
            print("\nCongratulations, you can date my granddaughter")

        else:
            # Display if user age as int does not make sense
            if (user_guess_as_int <= 0 or user_guess_as_int >= 120):
                print("\n{} is not a valid age.".format(user_guess_as_int))

            # Display if user age as int is too young
            elif (user_guess_as_int <= 25):
                print("\n{} is too young for my granddaughter.".format(user_guess_as_int))

            # Display if user age as int is too old
            else:
                print("\n{} is too old for my granddaughter.".format(user_guess_as_int))

    # Display a message to the user if they entered something that is not valid
    except Exception:
        # Message for incorrect user input
        print("\n{} is not a valid age.".format(user_age_as_string))

    # finally statement
    finally:
        # Display thank you message to user
        print("\nThank you for playing")


if __name__ == "__main__":
    main()
