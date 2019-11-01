#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: November 2019
# This program adds an amount of numbers specified by the user


def main():
    # This function adds an amount of numbers specified by the user

    # Variables
    sum_of_numbers = 0

    # Input
    adding_number = int(input("Enter the amount of numbers you want to add: "))
    print("")

    # Process
    for counter in range(adding_number):
        number = int(input("Enter a number to be added here: "))
        if number < 0:
            continue

        sum_of_numbers = sum_of_numbers + number

    # Output
    print("")
    print("The sum of your numbers is", sum_of_numbers)


if __name__ == "__main__":
    main()
