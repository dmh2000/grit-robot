import numpy as np


def R(x, y, theta):
    r = np.array([
        [np.cos(theta), -np.sin(theta), x],
        [np.sin(theta), np.cos(theta), y],
        [0, 0, 1]
    ])
    return r


p = np.array([1, 0, 1])
a = np.pi/4.0
r = R(1, 2, a)

p = r @ p
o = p[2] + a
print(p, o)
