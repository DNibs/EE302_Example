from ee302_example import print_polar
from ee302_example import print_cartesian
from ee302_example import polar
import math
import sympy as sym


# problem 1
def solve_problem_1(omega, vs):
    r210 = 210.
    l = 220e-3
    c = 27e-6
    r110 = 110.

    zl1 = complex(0, omega * l)
    zc1 = complex(0, -1 / (omega * c))

    z_eq = 1. / (1. / r210 + 1. / zl1 + 1. / zc1) + r110
    print_cartesian(z_eq, 'zeq')
    is1 = vs / z_eq
    print_polar(is1, 'is')
    vr110 = is1 * r110
    vr210 = vs - vr110
    print_polar(vr210, 'vr210')
    print_polar(vr210 / r210, 'ir210')
    print_polar(vr210 / zc1, 'ic')
    print_polar(vr210 / zl1, 'il')
    print_polar(vr210 / r210 + vr210 / zc1 + vr210 / zl1, 'check is')


omega1 = 120. * math.pi
vs1 = polar(170., 35.)
omega2 = 100. * math.pi
vs2 = polar(311., -110.)

print('Problem 1 a')
solve_problem_1(omega1, vs1)
print('\n\n')
print('Problem 1 b')
solve_problem_1(omega2, vs2)

# Problem 2
print('\n\n')
print('Problem 2')
is1 = polar(40e-3, -30.)
omega = 1800.*math.pi
vs2 = polar(24., 40.)
r160 = 160.
r200 = 200.
r130 = 130.
r82 = 82.
z_c = complex(0, -1 / (omega * 39e-6))
z_l12 = complex(0, omega * 12e-3)
z_l47 = complex(0, omega * 4.7e-3)

# Declare variables to solve
va, vb, vc = sym.symbols('va, vb, vc')

# Set up equations
eqnSN_AC = sym.Eq((va-vb)/r160 + (vc-vb)/r130 + vc/z_c + vc/(z_l12 + r82) , 0)
eqnCONS = sym.Eq(va-vc, vs2)
eqnB = sym.Eq(-is1 + vb/z_l47 + (vb-vc)/r130 + (vb-va)/r160, 0)

# Solve equations ad save the solution as an object called "solution"
solution = sym.solve([eqnSN_AC, eqnCONS, eqnB], (va, vb, vc))

print_polar(solution[va], 'va')
print_polar(solution[vb], 'vb')
print_polar(solution[vc], 'vc')

# Problem 3
print('\n\n')
print('Problem 3')

# Declare variables to solve
iw, iy, iz = sym.symbols('iw, iy, iz')

# Set up equations
eqnW = sym.Eq(r130*(iw-iy) + r160*iw + vs2, 0)
eqnY = sym.Eq(z_l47*(iy-is1) + r130*(iy-iw) + z_c*(iy-iz), 0.)
eqnZ = sym.Eq(z_c*(iz-iy) + z_l12*iz + r82*iz, 0)

# Solve equations ad save the solution as an object called "solution"
solution = sym.solve([eqnW, eqnY, eqnZ], (iw, iy, iz))

print_polar(solution[iw], 'iw')
print_polar(solution[iy], 'iy')
print_polar(solution[iz], 'iz')

