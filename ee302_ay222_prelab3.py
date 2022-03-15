import sympy as sym

vs1 = 6.
r1 = 300.
r2 = 1300.
r3 = 390.
r4 = 1100.
rl = 820.


# Declare variables to solve
va, vb = sym.symbols('va, vb')

# Set up equations
eqn_a = sym.Eq((va-vs1)/r1 + va/r2 + (va-vb)/r3, 0)
eqn_b = sym.Eq((vb-va)/r3 + vb/r4, 0)

# Solve equations ad save the solution as an object called "solution"
solution_nva = sym.solve([eqn_a, eqn_b], (va, vb))
print(solution_nva)

vt = solution_nva[vb]

v_norton = sym.symbols('v_norton')
eqn_norton = sym.Eq((v_norton-vs1)/r1 + v_norton/r2 + v_norton/r3, 0)
solution_norton = sym.solve([eqn_norton], v_norton)

i_norton = solution_norton[v_norton] / r3
print('i_norton = ', i_norton)
req = vt / i_norton
print('req = ', req)

req_check_tmp = (r1**(-1)+r2**(-1))**(-1)+r3
req_check = (req_check_tmp**(-1)+r4**(-1))**(-1)
print(req_check)

v_load = vt*(rl/(req+rl))
print('vload ', v_load)

i_load = vt / (req + rl)
print('i_load = ', i_load)

p_max = (vt/2) * (vt/(2*req))
print('p_max = ', p_max)
