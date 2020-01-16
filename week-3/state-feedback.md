# STATE FEEDBACK

assume access to full state

x_dot = Ax + Bu
u = -Kx
x_dot = Ax + -BKx
A_hat = (A - BK)x : closed loop dynamics

now, pick K such that closed loop system is stabilized
R: eig(A-BK) < 0

B = 2x1
K = 1x2
A = 2x2

A - BK = [[0,1],[0,0]] - [[0],[1]] @ [[k1,k2]]
x_dot = [[0,1],[-k1,-k2]] @ x

k1 = k2 = 1
k1 = 0.1, k2 = 1

see e.py

some eigenvalues are better than others
next : pick eigenvalues and control lawys based on output rather than state
