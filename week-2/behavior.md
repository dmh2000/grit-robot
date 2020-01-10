# Behavior-based

rather than continually plan, use behaviors
to adapt to current situation

develop a library of useful controllers
switch controllers in response to environment

assume

- a differential drive, wheeled robot
- constant speed
- x_dot = v0 cos(phi)
- y_dot = v0 sin(phi)
- phi_dot = omega

phi : current heading
phi_d : desired heading
figure out omega

## Dealing with Angles

naive implementation doesn't work because we are working with angles
ensure error is aways e = [-pi,pi]
e' = atan2(sin(e),cos(e))

# implementation

- reference:
  - r = phi_d
- error
  - e = phi_d - phi
  - e' = atan2(sin(e),cos(e))
- phi_dot
  - omega

control with omega (phi_dot) ?

- e'dot = e' / dt
- E = E + e'
- omega = k_p \* e' + k_i \* E + k\*d \* e'dot
- old_e' = e'

# two behaviors

- go-to-goal
- avoid-obstacles
