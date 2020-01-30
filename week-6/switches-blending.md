# hard switches and blending

How to combine behaviors

- Hard switch
  - pro : performance guarantee
  - con : bumpy ride, Zeno?
  - designing behaviors to do something really well
- Blended Behaviors

  - pro : smooth ride
  - con : no guarantees it will get to the goal and not hit obstacles

- Switched Hybrid Automaton

  - u_gtg= K_gtg(x_g - x)
  - x_dot = u
  - u_ao - K_ao(x - x_o)

- Blending Function
  - sigma(d_o) E [0,1]
  - sigma = amount goal to goal
  - 1-sigma = amount avoid obs
  - x_dot = sigma u_gtg + (1-sigma)u_ao
