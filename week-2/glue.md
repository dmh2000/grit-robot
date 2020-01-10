# week 2 glue

robot models

two models for robots:

- differential drive vr,vl
  - x_dot = R/2(V_r + V_l) cos(phi)
  - y_dot = R/2(V_r + V_l) sin(phi)
  - phi_dot = R/L(V_r - V_l)
- unicycle model v,omega
  - where am i and where am i pointing
  - x_dot = v cos(phi)
  - y_dot = v sin(phi)
  - phi_dot = w

## go from unicycle model to differential drive model

- model with unicycle
  - v,w
- commands to robots
  - v_r
  - v_l
- transform

  - v_r = (2v + wL) / 2R
  - v_l = (2v - wL) / 2R
  -

- example
- v = 0
- w = constant
- mapping

  - v_r = wL / 2R
  - v_l = -wl / 2R

- example
- A = robot
- B = goal
- t = 10
- v = B-A/10
- omega = 0

## feedback required for control

## wheel encoders

- D_l : 2piR(dtick_left/N)
- D_r : 2piR(dtick_right/N)
- D_c : (D_l + D_r) / 2 (center)

- x' = x + Dc cos(phi)
- y' = y + Dc sin(phi)
- phi' = phi + (D_r - D_l) / L

V = wR : linear velocity from angular velocity
Distance = wR \* dt
D_r = R v_r dt
D_l = R v_l dt

v_r = D_r / (R \* dt)
v_l = D_l / (R \* dt)

x(t + dt) = x(t) + x_dot\*dt

if robot starts at origin, where is it located afte r0.1s
dtick_r = 10
dtick_l = 6
R = 2m
total ticks = 100
L = 4m
