#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: March 2022
# This program calculates the surface area and
#     volume of a rectangular pyramid

import math


def main():
    # This function calculates volume and surface area

    # Input
    height = int(input("Enter height of pyramid (cm): "))
    length = int(input("Enter length of pyramid (cm): "))

    # Process
    volume = 1 / 3 * height * length**2
    surfaceArea = length**2 + (
        2 * length * math.sqrt((length**2) / 4 + height**2)
    )

    # Output
    print("")
    print("Volume: {:0.0f} cm³.".format(volume))
    print("Surface area: {:0.2f} cm².".format(surfaceArea))

    print("\nDone.")


if __name__ == "__main__":
    main()
