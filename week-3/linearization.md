# linearization

'almost everything is non-linear'

many nonlinear systems are linear within a range of operation

x_dot = f(x,u)
y = h(x)

find local linear model around operating point : taylor series

operating point = (x0,u0) -> (x = x0 + dx), (u = u0 + du)

equations of motion
dx_dot = x_dot = x0_dot = x_dot = f(x0+dx,u0+du)

partial derivatives (jacobian)
small dx,du are ~linear around the operating point

dx_dot = f(x0,u0) + df/dx(x0,u0)dx + df/du(x0,u0)du ...hot
A = df/dx(x0,u0)dx
B = df/du(x0,u0)du
u = h(x0+dx) = h(x0) + dh/dx(x0)dx ...hot
assume
f(x0,u0) = 0
h(x0) = 0

dx_dot = Adx + Bdu
y = Cdx
A = df/dx(x0,u0)
B = df/du(x0,u0)
C = dh/dx(x0)

**inverted pedulum**
theta_dot_dot = g/l\*sin(theta) + u\*cos(theta)

x1 = theta
x2 = theta_dot
y = x1

f(x,u) = [
x2,
g/l \* sin(x1) + u \* cos(x1)
]
h(x) = x1

operating point = (x0,u0) = (0,0)

**unicycle model**
naive linearization doesn't work
