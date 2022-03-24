# Component Values
vcc_pos = 12.
vcc_neg = -10.
r1 = 13e3
r2 = 36e3
r3 = 43e3

# noninverting amp
gain_noninverting = 1 + r2 / r1
print("noninverting gain = ", gain_noninverting)

# inverting amp
gain_inverting = - r3/r1
print("inverting gain = ", gain_inverting)

v_in = list(range(-4, 5))
print(v_in)

v_out = []
for v in v_in:
    v_out.append(v * gain_inverting)
print(v_out)


