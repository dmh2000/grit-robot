# SEGWAY ROBOTS

if a system is not CC, you have to buy a bigger and better B Matrix

- segway robot
  - inverted pendulum
  - on top of unicycle

## Base

- x_dot1 = v cos psi
- x_dot2 = v sin psi
- psi_dot = omega

Pendulum

- [phi,phi_dot]
- inputs torques TL,TR
-

State

- x = [x1,x2,v,psi,psi_dot,phi,phi_dot]
- u = [TL,TR}]
- x_dot = f(x,u)
  - vcos(psi), vsin(psi), v_dot,psi_dot,psi_dot_dot,phi_dot,phi_dot_dot]T
- linearize

  - (x,y) = [0,0]
  - plug in physical parameters of the segway robot
  - x_dot = Ax + Bu

- Controllability of segway

  - rank = 6
  - n = 7
  - not CC
  - unicycle dynamics messed up when leinarized
  - if we can control v (velocity) and psi (turn rate), that should be enough
  - remove unicycle part
    - x = [v,psi,phi,phi_dot]T
    - u = [TL,TR]T
    - x_dot = Ax + Bu
  - do not stabilize around (v,omega) = (0,0)
  - let x_dot = x - [vd,omegad,0,0]T = x - delta

# Pole Placement
