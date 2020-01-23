import numpy as np


def gamma(A, B):
    print(A@B)
    G = np.array([B, A@B])
    G = G.squeeze()
    print('gamma', G)
    print('rank', np.linalg.matrix_rank(G))


# A = np.array([
#     [2, 0],
#     [1, 1]
# ])
# B = np.array([[1], [1]])
# gamma(A, B)
# print()
# A = np.array([
#     [0, 1],
#     [0, 0]
# ])
# B = np.array([[0], [1]])
# gamma(A, B)
A = np.array([
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
])
B = np.array([
    [0], [1], [0], [0]
])
u = 2


a = np.linalg.eig(A)
print(a)

print(A@A)
gamma = np.array([
    B, A@B, A@A@B, A@A@A@B
])
print(gamma)
r = np.linalg.matrix_rank(gamma)
print(r)
gamma1 = gamma.reshape((4, 4))
print(gamma1)
r = np.linalg.matrix_rank(gamma1)
print(r)
gamma2 = gamma.squeeze()
print(gamma2)
r = np.linalg.matrix_rank(gamma1)
print(r)


B = np.array([[0, 0], [1, 0], [0, 0], [0, 1]])
# controllability matrix
gamma = np.array([
    B, A@B, A@A@B, A@A@A@B
])
gamma = gamma.reshape((8, 4))
r = np.linalg.matrix_rank(gamma)
print(gamma)
print(r)
