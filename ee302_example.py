# Example script for EE302 students unfamiliar with python
# Author: MAJ Niblick
# Date: 25APR2021
# Requires Python 3.8X or greater, numpy, sympy, and matplotlib

# To begin with, you'll need to download Python 3.8 or greater. Be sure to include pip in your options while installing
# Download an IDE - I like PyCharm, but Spyder is also popular
# Once you've done that, you'll need to install numpy, sympy, and matplotlib libraries for your project
# Some IDEs (such as pycharm) handle creating virtual environments so that each project is isolated from others,
#   making library dependencies a non-issue. It is often easy to install the above libraries through such IDEs.
# You could also use PIP in the terminal to install with the terminal like the following:
#   py -m pip install [library name]

# Import statements tell Python to use special libraries for this script (which we already installed to our environment)
# Specifically, we will import math for basic math functions, and cmath for complex functions.
# We will also import numpy for arrays, sympy for our equation solver, and matplotlib for plotting

import math
import cmath
import numpy as np
import sympy as sym
from matplotlib import pyplot as plt


# Next we define some custom helper functions

# By default, python uses radians instead of degrees. To avoid manually converting from degrees to
#   radians every time we want to input a polar number, this function simplifies it for us.
def polar(magnitude, degrees):
    """Converts polar number (magnitude, angle in degrees) to complex cartesian number"""
    return cmath.rect(magnitude, math.radians(degrees))


# The next two functions help us to conveniently format our answers for printing the console
def print_polar(complex_number, variable_name='', units='', significant_digits=3):
    """Prints complex number as polar in scientific format in degrees with optional variable name and units"""
    if variable_name != '':
        var_name = variable_name + ' = '
    else:
        var_name = ''
    mag = abs(complex_number)
    angle = math.degrees(cmath.polar(complex_number)[1])
    # python provides numerous options for modifying strings. Since 3.8, you can directly insert variables
    #   in a string using the f' ... {variable name} ...' option
    # Additionally, numeric variables can be formatted a certain way in a string by using the following way:
    #   variable:digits.digitsf, where digits is an integer to specify how many digits you want to display either
    #   before or after the period, and f stand for float (real number), or e for scientific exponential, or other
    #   numeric formatting styles
    print(f'{var_name}{mag:.{significant_digits-1}e} angle {angle:.{significant_digits-1}e} deg {units}')


def print_cartesian(complex_number, variable_name='', units='', significant_digits=3):
    """Prints complex number as polar in scientific format in degrees with optional variable name and units"""
    if variable_name != '':
        var_name = variable_name + ' = '
    else:
        var_name = ''
    print(f'{var_name}{complex_number.real:.{significant_digits-1}e} + j'
          f'{complex_number.imag:.{significant_digits-1}e} {units}')


# Script stars here -------------------------------------------------------------------------------
if __name__ == "__main__":
    print('Part 1: Initializing and Printing Complex Numbers -----------------')
    # "complex" function is how you input a complex number. The first input is real, the second is imaginary
    vt = complex(5, 0)

    # Here are a few ways to print the complex variable. First is default print statement. second uses string formatting,
    # The other three use our custom functions above, with the last including the optional arguments.
    print(vt)
    print(f'vt = {vt} V')
    print_cartesian(vt)
    print_polar(vt)
    print_polar(vt, variable_name='vt', units='V', significant_digits=5)

    # Now we will define a variable by its polar coordinates instead of its cartesian coordinates using our custom function
    it = polar(.25, 30)
    print(it)
    print_cartesian(it)
    print_polar(it, variable_name='it', units='A', significant_digits=4)

    # Let's analyze some circuits!
    print('Part 2: Basic Analysis --------------------')
    # Say we have a simple circuit with a voltage source of 5angle0 V at 100 rad/s, a resistor of 100ohms,
    #   and a capacitor of 82 microFarads, all in series.
    vs = polar(5, 0)
    radians_per_second = 100
    r1 = 100
    c1 = 82e-6
    z_c = complex(0, -1/(radians_per_second*c1))

    # To find the voltage across the resistor, we can use voltage divider
    # Python follows normal order-of-operation conventions
    v_r1 = vs * r1 / (r1 + z_c)
    print_polar(v_r1, variable_name='v_r1', units='V')

    print('Part 3: Solving Systems --------------------')
    # To solve a system of equations for nodal voltage analysis or mesh analysis, we can use sympy's solve function
    # Say we have to solve a circuit with the following equations:
    # eqn1 = (va-5)/r1 + (va-0)/r2 + (va-vb)/z_c == 0
    # eqn2 = (vb-va)/z_c + (vb-0)/r3
    vs = 5
    r1 = 100
    r2 = 200
    r3 = 150
    z_c = complex(0, -1/(100*82e-6))

    # Declare variables to solve
    va, vb = sym.symbols('va, vb')

    # Set up equations
    eqn1 = sym.Eq((va-vs)/r1 + (va-0)/r2 + (va-vb)/z_c, 0)
    eqn2 = sym.Eq((vb-va)/z_c + vb/r3, 0)

    # Solve equations ad save the solution as an object called "solution"
    solution = sym.solve([eqn1, eqn2], (va, vb))
    print(solution)

    # To call out a specific variable from solution, use solution[variable]
    print(solution[va])

    # Notice that solution is a string, not a complex number. We can't us it in any follow on math! To fix that,
    #   we can convert the string to a complex number with the 'complex()' function
    va = complex(solution[va])
    print(va)
    print_polar(va, variable_name='va', units='V')

    # Let's plot some results!
    print('Part 4: Plotting ------------------------')
    # We have a series circuit of voltage source and two resistors, r1 and r_load
    # We want to change a load resistor to see how the power to the load changes
    # vs = 5V, R1 = 100 ohms - what happens to the power across RL as we adjust the resistance?
    vs = 5
    r1 = 100

    # Python needs discrete values to plot, so we'll use numpy to create a range of r_load values
    #   from 80 to 120 in steps of 1
    # Note that when using numpy arrays in scalar math, the operations are applied to each element in the array
    r_load = np.arange(80, 120, 1)
    p_load = (vs*r_load/(r1+r_load)) * (vs / (r1+r_load))  # P = VI... terms are rearranged
    p_r1 = r1*(vs/(r1+r_load))**2

    # Create a "figure" object and an "axis" object to put on the figure
    fig, ax = plt.subplots()

    # Put data onto the x and y axis within our axis object
    # You can add multiple series of data to the same axis object
    ax.plot(r_load, p_load)
    ax.plot(r_load, p_r1)

    # Set some properties for our axis object, such as labels
    ax.set_xlabel('$R_L$ (ohms)')  # Using dollar signs in matplotlib gives the formatting a "math" style similar to LaTex
    ax.set_ylabel('Power (watts)')
    ax.set_title('Power Across Resistors in Series')
    ax.legend(['$R_L$', '$R1$'])
    # ax.set_xlim(90, 110)  # Sets limits on x-axis
    ax.set_ylim(0.06, 0.065)  # Sets limits on y-axis

    # Show on the screen
    plt.show()

    # Congratulations!
