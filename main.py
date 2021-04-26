# Example script for EE302 students unfamiliar with python
# Author: MAJ Niblick
# Date: 25APR2021
# Requires Python 3.8X or greater, numpy

# First are import statements which tell Python to use additional libraries.
# Specifically, we will import math for basic math funcitons, and cmath for complex functions.

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


def print_polar(complex_number, variable_name='', units='', significant_digits=3):
    """Prints complex number as polar in scientific format in degrees with optional variable name and units"""
    if variable_name != '':
        var_name = variable_name + ' = '
    else:
        var_name = ''
    mag = abs(complex_number)
    angle = math.degrees(cmath.polar(complex_number)[1])
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
print('Part 1: Initializing and Printing Complex Numbers -----------------')
# "complex" function is how you input a complex number. The first input is real, the second is imaginary
vt = complex(5, 0)

# Here are a few ways to print the complex variable. First is default print statement.
# The other three use our custom functions above, with the last also using the optional arguments.
print(vt)
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

# To find the voltage across the resistor, we can voltage divider
v_r1 = vs * r1 / (r1 + z_c)
print_polar(v_r1, variable_name='v_r1', units='V')

print('Part 3: Solving Systems --------------------')
# To solve a system of equations for nodal or mesh analysis, we can use sympy's solve function
# Set up your equations as a matrix multiplication, like the following:
# Say we have to solve a circuit with the following equations
# eqn1 = (va-5)/r1 + (va-0)/r2 + (va-vb)/z_c == 0
# eqn2 = (vb-va)/z_c + (vb-0)/r3
r1 = 100
r2 = 200
r3 = 150
z_c = complex(0, -1/(100*82e-6))

# Declare variables to solve
va, vb = sym.symbols('va, vb')

# Set up equations
eqn1 = sym.Eq((va-5)/r1 + (va-0)/r2 + (va-vb)/z_c, 0)
eqn2 = sym.Eq((vb-va)/z_c + vb/r3, 0)

# Solve equations ad save the solution as an object called "solution"
solution = sym.solve([eqn1, eqn2], (va, vb))
print(solution)

# To call out a specific variable from solution, use solution[variable]
print(solution[va])

# Notice that solution is actually formatted as a string, not a complex number. To do use the solution
#   as a complex number from this point on, we can convert it with the 'complex()' function
va = complex(solution[va])
print(va)
print_polar(va, variable_name='va', units='V')

# Let's plot some results!
print('Part 4: Plotting ------------------------')
# We have a fixed circuit and want to change a load resistor to see how the power to the load changes
# vs = 5V, R1 = 100 ohms - what happens to the power across RL as we adjust the resistance?
vs = 5
r1 = 100
r_load = np.arange(80, 120, 1)
p_load = (vs*r_load/(r1+r_load)) * (vs / (r1+r_load))
fig, ax = plt.subplots()
ax.plot(r_load, p_load)
ax.set_xlabel('r_load (ohms)')
ax.set_ylabel('p_load (watts)')
ax.set_title('Power Across Load Resistor')
ax.set_xlim(90, 110)  # Sets limits on x-axis
plt.show()

