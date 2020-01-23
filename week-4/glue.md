# WEEK 4 Glue - Controllability and Observability

## System Stability

robot arm
x = [
theta1,
theat1_dot,
theta2,
theta2_dot
]

A = [
[0,1,0,0],
[0,0,0,0],
[0,0,0,1],
[0,0,0,0]
]

x_dot = Ax

check eigenvalues of A
they are all 0, system is unstable
introduce control

x_dot = Ax + Bu
we can control theta1_dot_dot
B = [0,1,0,0]
u = control signal
B \* u = [0,u,0,0]

create controllability matrix gamma
same number of terms as rows in A
gamma = [1@B, A@B, A^2@b A^3@B]
find rank of gamma
rank must equal same number of elements in gamma
if not, uncontrollable

Need more control
control theta1_dot_dot and theta2_dot_dot
B changes to:[[0,0],[1,0],[0,0],[0,1]]

x_dot = Ax + Bu
use state feedback

## state feedback

A = [[0,1],[0,0]]
B = [[0],[1]]
u = -Kx : design K to force eigenvalues to desired performance
x = [theta1,theta1_dot]
K = [k1,k2]
x_dot = (A - B@K)x
x_dot = ([[0,1],[0,0]] - [[0],[1]]@K)@x
x_dot = [[0,1],[-k1,-k2]]x
A' = x_dot
force stability with k1,k2
find eigenvalues

find determinant(A' - lambda@I)
use matlab symbolic charpoly
characteristic equation(L) = (L-l1)(L-l2)...(L-ln) = prod(L-li)
lambda^2 + k2lamba + k1
pick eigenvalues l1=-1,l2=-2
plug into equation
(lambda - l1)(lambda - l2) => (lambda + 1)(lambda + 2)
l^2 + k2l + k1
(l- -1)(l - -2)
(l + 1)(l + 2) => l^2 + 3l + 2
l^2 + k2l + k1
k2 = 3
k1 = 2

Assume we can see theta1
C = [1,0] choosing sensors
y = Cx

is it observable? estimate x_hat on observability matrix
omega = [[C],[CA]] = [[1,0],[0,1]]
rank of omega = 2
estimate:
x_hat_dot = Ax_hat + Bu + L(y - Cx_hat)
error dynamics:

- e_dot = x_dot = x_hat_dot = (A - LC)e
- force error to be stable, find L so error goes to zero

Execution
x_dot = Ax + Bu, y = Cx (Plant)
x = [theta1,theta1_dot]
A = [[0,1],[0,0]]
B = [0,1]
C = [1,0]
its controllable(K) and observable(L)

a) wake up t = t0, x = x0, x_hat = x_hat0
b) loop in dt increments
c) read output
d) compute control u = -K @ x_hat (initial estimate)
e) send control u
f) update x_hat using dynamics x_hat_dot = Ax_hat + Bu + L(y - Cx_hat)
g) x_hat = x_hat + dt \* x_hat_dot
h) repeat
