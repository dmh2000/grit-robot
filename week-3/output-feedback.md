# OUTPUT FEEDBACK

eigenvalues should have negative real parts

x_dot = Ax + Bu
y = Cx + Du

u ----+----> x_dot = Ax + Bu , y = Cx + Du ----+----> y
^ |
|----------------------------------------|

point on a line

p_dot_dot = u (feedback)
x_dot = [
0,1
0,0
] @ x + [0,1] @ U
y = [1,0] @ x

move towards origin
u > 0 if y < 0
u < 0 if y > 0
y = -y

u = -Ky = -KCx
x_dot = Ax + Bu
x_dot = Ax - BKCx = (A - BKC)x
A_hat = A - BKC
K = 1

find eigenvalues

A_hat = [[0,1],[0,0]] - [[0],[1]] @ [[1,0]]
scipy.linalg.eig(A_hat) = (0+j,0-j)

two purely imaginary and no real parts => critically stable (will oscillate)

- import scipy.linalg as la
- B = np.array([[0],[1]])
- A = np.array([[0, 1],[0, 0]])
- C = np.array([[1, 0]])
- A_hat = A - B @ C
- A_hat
- array([[ 0, 1],
- [-1, 0]])
- la.eig(A_hat)
- (array([0.+1.j, 0.-1.j]), array([[0.70710678+0.j , 0.70710678-0.j ],
- [0. +0.70710678j, 0. -0.70710678j]]))

- doesn't use velocity, only acceleration
- velocity is not available
- need full state information
- get velocity by (x_1 - x_0)/dt
- we don't know x, we know y
