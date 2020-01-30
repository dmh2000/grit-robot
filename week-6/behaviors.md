# Behaviors/planning

a behavior is a subsystem/controller

## planning

x_dot = u,x ∈ R2

x_dot = [0,0;0,0] x + I@u
Γ = [B AB] = [I 0] rank(Γ) = 2
completely controllable

Behaviors

- ## go to goal
- Go To Goal
  - pick a motion vector (direction and magnitude)
  - set x_dot = u
  - e = x_g - x
  - e_dot = -Ke
  - u = Ke -> e_dot = 0 - x_dot = -Ke
  - asymptotically stable?
  - K > 0 or eig(K) > 0
  - e -> 0
  - in practice make K a function of e
  - e_dot = -K(||e||)e
  - K = v0 (1-e^(-alpha||e||^2))
  - exponential decay
- Avoid Obstacle
  - flip the sign in the go-to-goal behavior
  - x_0 = obstacke
  - e = x - x0
  - vector pointing away from obstacle
  - u = Ke => e_dot = Ke (unstable!)
  - u = K(x - x0)
  - solution
  - make K dependent on distance to e
  - use the induced mode
  - K = 1 ..........c
  - ..------ ---------------------
  - ..norm(e) (norm(e)^2 + epsilon))
  - dont care when far away
  - care more when close
- ALso
  - couple actual robot dynamics to the behaviors
  - figure out mode transitions
  -
