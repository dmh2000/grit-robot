# boundary following

- Wall Following
- flip U_ao 90 deg to u_fw

u_fw = alpha[0,1;-1,0]u_ao = alphaR(-pi/2)u_ao
rotation matrix for pi/2 rotation

u_c_fw : clockwise -pi/2 rot
u_cc_fw : counterclockwise pi/2 rot
R(t) = [cos(t),-sin(t);sin(t),cos(t)]

u_cfw = alpha R(-pi/2)u_ao = alpha[0,1;-1,0]u_ao
u_ccfw = alpha R(pi/2)u_ao = alpha[0,-1;1,0]u_ao

- which way to follow?

  - let go-to-goal decide which way to go
  - get go-to-goal angle
  - inner product
    - <v,w> = v.T w = ||v|| ||w|| cos(angle(v,w))
    - <u_gtg,u_cfw> > 0 => u_cfw
    - <u_gtg,u_ccfw> > 0 -> u_ccfw

- when to release wall follow
  - aR(+-pi/2)u_ao
