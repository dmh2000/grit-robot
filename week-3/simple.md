# a simple robot

## models

- general
- simple
- expressive
- relevant

## Linear Systems

point mass controlled by acceleration
p = position
u = acceleration (p_dot_dot)

### general form

- x1 = p
- x2 = p_dot
-
- x1_dot = x2
- x2_dot = u

### state space form

1D point mass

- x = [x1, x2]
- x_dot = [x1_dot, x2_dot] = [x2, u]

x_dot = [x1_dot, x2_dot] = [x2, u]

state space form
A = [  
 [0, 1][0, 0]
]
B = [0, 1]
C = [1, 0]

x_dot = A @x + B @ u

y = p = x1 = C @ x

2D point mass

P_x_dot_dot = u_x
p_y_dot_dot = u_y
u = [u_x,u_y] acceleration
p = [p_x,p_y] position

x1 = p_x
x2 = p_x_dot
x3 = p_y
x4 = p_y_dot
u1 = u_x
u2 = u_y
y1 = p_x
y2 = p_y

A = [
0,1,0,0 (x velocity)
0,0,0,0
0,0,0,1 (y velocity)
0,0,0,0
]

B = [
0,0
1,0 (x acceleration)
0,0
0,1 (y acceleration)
]

C = [
1,0,0,0 (x position)
0,0,1,0 (y position)
]

x_dot = Ax + Bu
y = Cx

**Linear Time Invariant in State Space Form**

matrix sizes
x = Rn  
u = Rm
y = Rp
A = nxn
B = nxm
C = pxm

(nxn)(nx1) -> nx1
(nxm)(mx1) -> nx1
(pxn)(nx1) => px1
