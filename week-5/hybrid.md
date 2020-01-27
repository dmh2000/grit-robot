# Hybrid Automata

- models with continuous dynamics and discrete switch logic
- finite state machine
  - continuous dynamics
  - discrete logic
- continuous state X
- discrete state Q
  - which mode
  - x_dot = f_q(x,u)
- transition between different discrete modes
- We need
- Dynamics
  - for each state
- Guard:
  - check when to change state
  - x E Gq_q'
- Reset
  - handle abrubt transition
  - x = Rq_q'(x)

## Hybrid Automaton Model

- q = current state
- G(a,b) check for transition from a to b
- R(a,b) handle switch from a to b
  q = 1
  switch(q)
  case 1:
  if x in G(1,2)
  execute R(1,2)
  q = 2
  case 2:
  if x in G(2,3)
  execute R(2,3)
  q = 3
  ...

Guard should have hysteresis

- T >= T_d + epsilon : go to heat
- T <= T_d - epsilon : go to cool

Goal to Goal state
x_dot = f_gtg(x)
if x_dot too close to obstacle
switch to avoid obstacle
Avoid Objstacle state
if x_dot far enough from obstacle
switch to goal to goal
