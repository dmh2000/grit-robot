import numpy as np
# question 2


def obs(A, C):
    omega = np.array([[C], [C@A]])
    omega = omega.squeeze()
    r = np.linalg.matrix_rank(omega)
    print(C)
    print(r)
    return r


A = np.array([[0, 1], [0, 0]])
C = np.array([0, 1])
obs(A, C)
C = np.array([-1, 0])
obs(A, C)
C = np.array([1, -1])
obs(A, C)
C = np.array([1, 0])
obs(A, C)
C = np.array([1, 1])
obs(A, C)


print("------------------------------------")
t = 0
x_hat = 1
dt = 0.1
u = 1
K = 5
x_hat_dot = 0
X = []
while(t < 1.0):
    u = -K * x_hat
    x_hat_dot = 2*x_hat + u
    x_hat = x_hat + x_hat_dot * dt
    X.append(x_hat)
    t = t + dt
print(x_hat)
