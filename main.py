# Example script for EE302 students unfamiliar with python
# Author: MAJ Niblick
# Date: 25APR2021

# First are import statements which tell Python to use additional libraries.
# Specifically, we will import math for basic math funcitons, and cmath for complex functions.

import math
import cmath


# Next we define some basic helper functions of our own

# By default, python uses radians instead of degrees. To avoid having to convert from degrees to
#   radians every time we want to input a polar number, this function simplifies it for us.
def polar(magnitude, degrees):
    """Converts polar number (magnitude, angle in degrees) to complex cartesian number"""
    return cmath.rect(magnitude, math.radians(degrees))


def print_polar(complex_number, variable_name='', units='', significant_digits=3):
    """Prints complex number as polar in degrees with optional variable name and units"""
    mag = abs(complex_number)
    angle = math.degrees(cmath.polar(complex_number)[1])
    print(f'{variable_name} = {mag:.{significant_digits}e} angle {angle:.{significant_digits}e} {units}')


if __name__ == '__main__':
    vt = complex(5, 2)
    print_polar(vt, variable_name='Vt', units='V')
