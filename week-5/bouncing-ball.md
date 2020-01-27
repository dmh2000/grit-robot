# Bouncing Ball

drop a ball dropped on a surface

- ball

  - h above ground
  - h_dot_dot = -g
  - falling
    - x_dot = [[0,1],[0,0]x + [0,-g]
    - y = [1,0]x
  - bounce
    - inelastic bounce
    - h_dot = -gamma \* h_dot
    - x = [[1,0],[0,-gamma]]x

- x_dot = Ax + b
- A = [[0,1],[0,0]], b = [0,-g]
- R = [[1,0],[0,-gamma]]
- G = h <= 0 and h_dot <= 0
- LTI analysis
  - e^at = I + At + 0 = [[1,t],[0,1]]
  - h_0 + h_dot_0(t - t_0) - g/2(t-t_0)^2
- time in between bounces
  - T = 0, T = 2h_dot_0/g
- accumulated bounce times
  - T1 = 2v/g
  - T2 = 2v/g + gamma\*2v/g
  - Tn = 2v/g \* gamma_k
  - T_inf = (2v/g) \* 1/(1-gamma) < infinity
  - the ball bounces an infinite number of times in finite time
    - simulation wil crash
    - hybrid system undefined beyhond this time
    - Zeno phenomenom
