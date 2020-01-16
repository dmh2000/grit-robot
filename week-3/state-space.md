# state space models

x_dot = A@x + B@u (velocity)
y = Cx (estimated position)

Ax = physics of system
Bu = how input affects the state
Cx = encodes sensors (what is measured)

u -> state space model -> y
how to select input 'u'

**car model**
x = velocity
v_dot = (c/m)u - gamma\*v
x_dot = Ax + Bu
y = Cx

A = -gamma
B=C/m
C = 1

x = [v], A = -gamma
u = [u], B = c/m
x = [v], C = 1

**pendulum**
theta_dot_dot = -(g/l) * sin(theta) + c*u
nonlinear

linearize : small angle sin(theta) = theta

x = [theta,theta_dot]
A = [
0,1
-g/l, 0
]
B= [0,c]
C = [1,0]

**two robots on a line**
velocity control
x1 = position robot 1
x2 = position robot 2
x_1_dot = velocity robot 1
x_2_dot = velocity robot 2

A = 0
B = [
1,0
0,1
]
x_dot = [0] + B @ u

**rendezvous problem**
u1 = x2 - x1 (difference in position)
u2 = x1 - x2

x_dot = [
-1,1
1,-1
] @ u

**unicycle robot**
