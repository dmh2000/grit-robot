# controllability

B matrix represents the actuators

- when can we place the eignevalues how we want
- when is the B matrix rich enough (actuators
- controllability)

X_1 = Ax + Bu, X0 = 0
in n steps, drive it to a target state

x_1 = Ax0 + Bu0 = BU0
X_2 = Ax1 + Bu1 = ABu0 + BU1
X_3 = Ax2 + Bu2 = A^2Bu0 + Abu1 + Bu2

solve
x_star = [ B AB ... An-1B][un-1,...u1,u0]
gamma (n x nm)

this is possible for any target state if and only if
rank(gamma) = n

x_dot = Ax + Bu

## Definition of Controllability

this system is completely controllable (CC) if it is possible to go
from any initial state to any find state
gamma = [B AB ... A^n-1B] controllability matrix

## CC Theorem 1

- the system is CC if an only if rank(gamma) = n
- rank : max number of linearly independent rows or columns

two systems

- x_dot = [[2,0],[1,1]]x + [1,1]u : pole placement not possible
  - n = 2 gamma = [B, AB]
  - AB [2,2] gamma = [[1,2],[1,2]]
  - rank = 1 linearly independent column
- x_dot = [[0,1],[0,0]]x + [0,1]u : pole placement possible
  - n = 2 gamma = [B, AB]
  - AB[1,0] gamma = [[0,1],[1,0]]
  - rank = 2 linearly independent columns

## CC Theorem 2

- pole placement to arbitrary eigenvalues is possible if and only the system is CC
- need to check if a system is controllable
- matlab

  - G=ctrb(A,B)
  - rank(G)
  -

- if a system is CC
  - it can go between arbitrary points
  - but doesn't mean you can follow any trajectory
