import numpy as np
import scipy.linalg as la


def e(k1, k2):
    A = np.array([[0, 1], [-k1, -k2]])
    print(A)
    e = la.eig(A)
    print(e[0])
    return e


def f(a, b):
    A = np.array([[a, b], [0, a]])
    print('a', A)
    e = la.eig(A)
    print('e', e[0])
    return e


# k1 = P
# k2 = D
# attempt 1
# asymptotically stable, oscillates
# e(1, 1)
# [[0  1]
# [-1 - 1]]
# [-0.5+0.8660254j - 0.5-0.8660254j]
# attempt 2
# asymptotically stable, no oscillations
# converges very slowly
# e(0.1, 1)
# [[0.   1.]
#  [-0.1 - 1.]]
# [-0.11270167+0.j - 0.88729833+0.j]
print()
f(2, -1)
print()
f(-1, 2)
print()
f(-2, -2)
print()
f(-1, 5)
print()
f(-1, 100)
print()
