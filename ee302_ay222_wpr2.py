from ee302_example import print_polar
from ee302_example import print_cartesian
from ee302_example import polar
import math
import sympy as sym

# Problem 1
print('Problem 1')
period = .02
freq = 1 / period
radians = freq * 2. * math.pi
amp = 3.
phase_in_time = .01
phase_in_degrees = phase_in_time / period * 360.
print('amplitude = ', amp)
print('radians = ', radians)
print('phase = ', phase_in_degrees)

print('Bonus: you can do - or + 180 degrees for phase, or do - amplitude with 0 phase - all give same math result')

# Problem 2
print('Problem 2')
print('False, False, True, False, True')

# Problem 3
print('Problem 3a')


def impedance_of_capacitor(capacitance, omega):
    return complex(0, -1. / (capacitance*omega))


def impedance_of_inductor(inductance, omega):
    return complex(0, inductance*omega)


inductance = 12.e-3
r1 = 330.
zeq20 = (r1 * impedance_of_inductor(inductance, 20.e3)) / (r1 + impedance_of_inductor(inductance, 20.e3))
zeq40 = (r1 * impedance_of_inductor(inductance, 40.e3)) / (r1 + impedance_of_inductor(inductance, 40.e3))
zeq80 = (r1 * impedance_of_inductor(inductance, 80.e3)) / (r1 + impedance_of_inductor(inductance, 80.e3))

print_cartesian(zeq20, 'zeq20')
print_cartesian(zeq40, 'zeq40')
print_cartesian(zeq80, 'zeq80')
zeq20v2 = (r1**-1 + impedance_of_inductor(inductance, 20.e3)**-1)**-1

print('Problem 3b')
i_d = polar(5, 0) / impedance_of_inductor(inductance, 40.e3)
print_polar(i_d, 'i_d')

# Problem 4
print('Problem 4')
rf = 8.e3
r1 = 4.e3
r2 = 8.e3
r3 = 2.e3
v1 = 3.
v2 = 5.


def p4_opamp_output(v_in):
    return -(v1*rf/r1 + v2*rf/r2 + v_in*rf/r3)


print(p4_opamp_output(-3.))
print(p4_opamp_output(-1.))
print(p4_opamp_output(0.))
print(p4_opamp_output(1.))
print(p4_opamp_output(3.))

# Problem 5
print('Problem 5a')
omega = 120. * math.pi * 2.
vs1 = polar(10, 0)
vs2 = polar(12, 62)
z_c = impedance_of_capacitor(270.e-6, omega)
z_l_11 = impedance_of_inductor(11.e-3, omega)
z_l_21 = impedance_of_inductor(21.e-3, omega)

print_cartesian(z_c, 'z_c')
print_cartesian(z_l_21, 'z_l_21')
print_cartesian(z_l_11, 'z_l_11')

print('Problem 5b')
# Declare variables to solve
va, vb = sym.symbols('va, vb')

# Set up equations
eqna = sym.Eq((va-vs1)/30. + va/56. + (va-(vb-vs2))/z_c, 0)
eqnb = sym.Eq(((vb-vs2)-va)/z_c + vb/z_l_21 + vb/(22.+z_l_11), 0)

print('(va-vs1)/30. + va/56. + (va-(vb-vs2))/z_c')
print('((vb-vs2)-va)/z_c + vb/z_l_21 + vb/(22.+z_l_11)')
# Solve equations ad save the solution as an object called "solution"
sol_nva = sym.solve([eqna, eqnb], (va, vb))

print('Problem 5c')
print_polar(sol_nva[va], 'va')
print_polar(sol_nva[vb], 'vb')

i_x = sol_nva[va]/56.
print_polar(i_x, 'ix')

print('Problem 5d')
print(abs(i_x) / math.sqrt(2))

print('Problem 6')
print('12V')
# See problem worked out on paper...
