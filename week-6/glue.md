# week-6 Glue

## Vectors for navigation

## behaviors

- gtg
- ao
- ucfw
- uccfw
- delta - distance from obstacle

- vectors:

  - u_gtg = Kgtg(x_goal - x)
  - u_ao = Kao(x-x_obs)
  - ucFW = alphaR(-pi/2)u_ao
  - uccFw = alphaR(pi/2)u_ao

- Rotation Matrix
- R(theta) = [cos(θ), -sin(θ);sin(θ),cos(θ)]

  - countercw R(p/2) = [0,-1;1,0]
  - clockwise R(-p/2) = [0,1;-1,0]
  - u_ccfw = alpha R(pi/2)u_ao = alpha[0,-1;1,0]u_ao
  - u_cfw = alpha R(-pi/2)u_ao = alpha[0,1;-1,0]u_ao

- state = (v,)
- start in gtg
  - compute vector towards goal
  - check if distance to obstacle = delta - epsilon
