import math
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ee302_example import print_polar
from ee302_example import print_cartesian
from ee302_example import polar

# Problem 1, V = 6cos(2pi50w), I=2cos(2pi50w - 36degrees)
voltage_amplitude = 6.
current_amplitude = 2.
current_phase = np.pi * 36. / 180.
freq = 50.
period = 1./freq
omega = 2. * freq * np.pi
left_limit = -.25*period
right_limit = 1.5*period
sampling = period / 100.
x = np.arange(left_limit, right_limit, sampling)
voltage = voltage_amplitude * np.sin(omega*x+np.pi/2.)
current = current_amplitude * np.sin(omega*x+np.pi/2. - current_phase)
power = abs(voltage * current)

minor_ticks = np.arange(left_limit, right_limit, period / 20.)

fig = plt.figure()
ax = fig.add_subplot()
linev, = ax.plot(x, voltage, label='v(t) [V]')
linei, = ax.plot(x, current, label='i(t) [A]')
# COMMENT OUT LINEP IF YOU DON'T WANT p(t) displayed
linep, = ax.plot(x, power, label='p(t) [W]')

ax.set_title('Voltage and Current through Load')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.grid(which='major', linewidth=1.5)
ax.grid(which='minor')
ax.axvline(0, color='k')
ax.axhline(0, color='k')
ax.set_xticks(minor_ticks, minor=True)
ax.legend()


# COMMENT BETWEEN DASHES IF YOU DON'T WANT ANIMATION --------------------
def animate(i):
    new_current = current_amplitude * np.sin(omega*x+np.pi/2. - i*np.pi/40.)
    linev.set_ydata(voltage_amplitude * np.sin(omega*x+np.pi/2.))
    linei.set_ydata(new_current)
    linep.set_ydata(abs(voltage * new_current))
    return [linev, linei, linep]


ani = animation.FuncAnimation(
    fig, animate, interval=80, blit=True, save_count=80)

ani.save('fig_over_time.gif')
# ------------------------------------------------------------


plt.show()

print('Problem 1')
print(' V = 6cos(2pi50w), I=2cos(2pi50w - 36degrees)')
v_1 = polar(6., 0.)
i_1 = polar(3., -36.)
z_1 = v_1 / i_1
inductor = z_1.imag / omega
print_cartesian(z_1, "impedance of load")
print(f'R = {z_1.real}')
print(f'Inductor = {inductor} H')

s_1 = v_1 * i_1.conjugate() / 2
print_cartesian(s_1, 'Complex power')
print(f'P aborbed by resistor = {s_1.real} W')
print('Real power absorbed by inductor = 0W')
pf = s_1.real / abs(s_1)
print(f'Power Factor = {pf}')
capacitance = s_1.imag/(abs(v_1)**2 * omega)
print(f'capacitance = {capacitance} F')

# Problem 2
print('\n\nProblem 2')
freq = 60.
omega = 2. * math.pi * freq
vs1 = polar(120.*math.sqrt(2), 0.)
is2 = polar(1.5*math.sqrt(2), 64.)
z1 = complex(5., -3.)
z2 = 4.
z3 = complex(2., 2.)
z4 = complex(0., -6.)
z5 = complex(18., -9.)
z6 = complex(12., 6.)

# Declare variables to solve
va, vb, vc = sym.symbols('va, vb, vc')

# Set up equations
eqn1 = sym.Eq((va-vc)/z3 + -is2, 0.)
eqn2 = sym.Eq(is2 + vb/z4, 0.)
eqn3 = sym.Eq((vc-vs1)/z1 + vc/z2 + (vc-va)/z3, 0.)

# Solve equations ad save the solution as an object called "solution"
solution = sym.solve([eqn1, eqn2, eqn3], (va, vb, vc))
print(solution)
vth = solution[va]-solution[vb]
print_polar(vth, 'Vth')

z_int = z1*z2/(z1+z2)
zth = z_int + z3 + z4 + z5 + z6
print_cartesian(zth, "Zth")
capacitance = -1./(zth.imag * omega)
print(f'resistor in zth = {zth.real} ohms')
print(f'capacitor in zth = {capacitance} F')
p_max = abs(vth)**2 / (4. * zth.real)
print(f'Max power transfer = {p_max} W')


# Problem 3
print('\n\nProblem 3')
n_pri = 2
n_sec = 10
vs = polar(120.*math.sqrt(2.), 0)
z1 = complex(10., 8.)
z2 = complex(0, -3.)
z3 = 20.
z4 = 10.
z5 = complex(0, 10.)

z_sec = z4*z5/(z4 + z5) + z3
z_pri = (n_pri/n_sec)**2 * z_sec
print_cartesian(z_pri, 'z_primary')
zeq = z_pri + z1 + z2
i_pri = vs / zeq
v_pri = vs - (i_pri * (z1 + z2))
print_polar(v_pri, 'V_primary')
print_polar(i_pri, 'I_primary')
v_sec = v_pri * n_sec / n_pri
i_sec = i_pri * n_pri / n_sec
print_polar(v_sec, 'V_secondary')
print_polar(i_sec, 'I_secondary')
s = vs * i_pri.conjugate() / 2.
print_cartesian(s, 'S')
