import numpy as np

distance = np.array([
    0.04,
    0.05,
    0.06,
    0.07,
    0.08,
    0.09,
    0.10,
    0.12,
    0.14,
    0.16,
    0.18,
    0.20,
    0.25,
    0.30
])

volts = np.array([
    2.750,
    2.350,
    2.050,
    1.750,
    1.550,
    1.400,
    1.275,
    1.075,
    0.925,
    0.805,
    0.725,
    0.650,
    0.500,
    0.400
])

countAdc = np.array([
    917,
    783,
    683,
    583,
    517,
    467,
    425,
    358,
    308,
    268,
    242,
    217,
    167,
    133
])


def polyAdcToDistance(countAdc, distance):
    v = countAdc * (3.0 / 1000.0)
    coeff = np.polyfit(v, distance, deg=4)
    return coeff


def convertAdcToDistance(coeff, d):
    return np.polyval(coeff, d)


c1 = polyAdcToDistance(countAdc, distance)
print(c1)
c2 = np.polyfit(countAdc, distance, deg=4)
print(c2)

d1 = convertAdcToDistance(c1, 2.75)
d2 = np.polyval(c2, 917)
print(d1, d2)
