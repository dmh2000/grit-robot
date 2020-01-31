import numpy as np

s2 = np.sqrt(2.0)
print(s2)
m = np.array([
    [1/s2, 1/s2],
    [-1/s2, 1/s2]
])

p = np.array([1, 0])

a = m @ p
print(a, np.arctan2(a[1], a[0]))
print(-np.pi / 4.0)
print(3*np.pi / 4)
print(-3*np.pi/4)
print(np.pi/4)
print(p / s2)
