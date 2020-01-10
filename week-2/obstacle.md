# obstacle avoidance

## states

- x : position
- y : position
- phi : heading

## implementation

w = phi_dot
v = ?
v_r = (2v + wL)/ 2R
v_l = (2v - wL) / 2R

## obstacle

robot = x,y
obstacle = x0,y0, phi_obs
goal = xg,yg

1. pure avoidance (pure)

- phi_1 = phi_obs + pi
- go directly away from obstacle

2. perpendicular (blended)

- phi_2 = phi_obs +- pi / 2
- add or subtract pi based on where the goal is

3. go to goa;

- ignore obstacles

4. blend goal + avoidance

- arbitration mechanisms
  - winner takes all = hard switches
  - blending = combined behaviors
  - performance : prefer blending
  - analysis : prefer hard switches
