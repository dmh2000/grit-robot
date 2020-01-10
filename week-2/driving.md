# DRIVING

1. models
2. sensors

Divide and conquer

- the world is dynamic and unknown
- the controller must respond to environment
- behaviors
  - multiple controllers
  - instead of replanning
  - go-to-goal
  - avoid obstacles
  - follow-wall
  - track-target
  - arcs

## Differential drive

- 2 wheels
- can turn at different rates (like a tank)
- controls
  - right wheel velocity
  - left wheel velocity

2 wheel differential drive model

- R : radius of wheels
- L wheelbase (distance between wheels)
- V_l, V_l : wheel rates
- states
  - x : position
  - y : position
  - phi : heading
  -

Unicycle Model

- control
  - v : forward velocity
  - w : omega : angular rate

Unicycle Model

- design for this model
- x_dot = v cos(phi)
- y_dot = v sin(phi)
- phi_dot = w

- v = R/2(v_r + v_l)
- w = R/L(v_r - v_l)
- 2v/R = V_r + V_l
- wL/R = v_r - v_l

## Final implementation model

transform and solve thise two linear equations for V_r and V_l
v_r = (2v + wL)/ 2R
v_l = (2v - wL) / 2R
L is known
R is known
w is computed by controller

Differential Drive Model

- implement this model
- x_dot = R/2(V_r + V_l) cos(phi)
- y_dot = R/2(V_r + V_l) sin(phi)
- phi_dot = R/L(V_r - V_l)
