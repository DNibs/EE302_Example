import sympy as sym

vs1 = 12.
vs2 = 6.
r1 = 1300.
r2 = 820.
r3 = 1600.
r4 = 1000.
r5 = 1500.


# Declare variables to solve
va, vb = sym.symbols('va, vb')

# Set up equations
eqn_a = sym.Eq((va-vs1)/r1 + va/r2 + (va-vb)/r3, 0)
eqn_b = sym.Eq((vb-va)/r3 + vb/r4 + (vb-vs2)/r5, 0)

# Solve equations ad save the solution as an object called "solution"
solution_nva = sym.solve([eqn_a, eqn_b], (va, vb))
print(solution_nva)

i1 = (vs1-solution_nva[va])/r1
i2 = solution_nva[va] / r2
i3 = (solution_nva[va] - solution_nva[vb]) / r3
i4 = solution_nva[vb] / r4
i5 = (solution_nva[vb] - vs2) / r5
print(i1, i2, i3, i4, i5)


ix, iy, iz = sym.symbols('ix, iy, iz')

eqn_x = sym.Eq(-vs1 + r1*ix + r2*(ix-iy), 0)
eqn_y = sym.Eq(r2*(iy-ix) + r3*iy + r4*(iy-iz), 0)
eqn_z = sym.Eq(r4*(iz-iy) + r5*iz + vs2, 0)

solution_mesh = sym.solve([eqn_x, eqn_y, eqn_z], (ix, iy, iz))
print(solution_mesh)
