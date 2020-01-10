import numpy as np
n = 100
R = 2
L = 4
x = 0.0
y = 0.0
phi = 0.0
dt = 0.1
dtick_r = 10
dtick_l = 6

D_l = 2 * np.pi * R * dtick_l / n
D_r = 2 * np.pi * R * dtick_r / n
D_c = (D_l + D_r) / 2

x = x + D_c * np.cos(phi)
y = y + D_c * np.sin(phi)
phi = phi + (D_r - D_l) / L
print(x, y, phi)
# =======================================================
n = 10
R = 0.1
L = 0.2
x = 0.0
y = 0.0
phi = 0.0
dt = 0.5
dtick_r = 5
dtick_l = 3

D_l = 2 * np.pi * R * dtick_l / n
D_r = 2 * np.pi * R * dtick_r / n
D_c = (D_l + D_r) / 2

x = x + D_c * np.cos(phi)
y = y + D_c * np.sin(phi)
phi = phi + (D_r - D_l) / L
print(x, y, phi)
# =======================================================

n = 10
R = 0.1
L = 0.2
x = 0.0
y = 0.0
phi = 0.0
dt = 300
dtick_r = 40
dtick_l = 65

D_l = 2 * np.pi * R * dtick_l / n
D_r = 2 * np.pi * R * dtick_r / n
D_c = (D_l + D_r) / 2

x = x + D_c * np.cos(phi)
y = y + D_c * np.sin(phi)
phi = phi + (D_r - D_l) / L
phi = np.arctan2(np.sin(phi), np.cos(phi))
print(x, y, phi)
