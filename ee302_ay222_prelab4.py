from ee302_example import print_polar
from ee302_example import print_cartesian
from ee302_example import polar
import math
import sympy as sym

vp = 3.
f = 1200.
r1 = 300.
r2 = 1000.
c1 = 0.39e-6
l1 = 100.e-3

z_c1 = complex(0, -1 / (f * 2 * math.pi * c1))
z_l1 = complex(0, f * 2 * math.pi * l1)

print_cartesian(z_c1, 'z_c')
print_cartesian(z_l1, 'z_l')

v_c1 = vp * z_c1 / (z_c1 + r1)
v_r1 = vp * r1 / (z_c1 + r1)
i_s = vp / (r1 + z_c1)
print_polar(v_c1, 'v_c1')
print_polar(v_r1, 'v_r1')
print_polar(i_s, 'i_s')

print_polar(v_c1 + v_r1, 'check addition vs vp')
# Declare variables to solve
va, vb = sym.symbols('va, vb')

# Set up equations
eqn_a = sym.Eq((va-vp)/z_c1 + va/r1 + (va-vb)/z_l1, 0)
eqn_b = sym.Eq((vb-va)/z_l1 + vb/r2, 0)

# Solve equations ad save the solution as an object called "solution"
solution_nva = sym.solve([eqn_a, eqn_b], (va, vb))
print(solution_nva)

print_polar(solution_nva[va], 'va')
print_polar(solution_nva[vb], 'vb')

print(1.89/math.sqrt(2))
print(1.51/math.sqrt(2))
