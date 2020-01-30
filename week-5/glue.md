# Glue for Hybrid Automata

## Hybrid Automata

construct an overall model
finite state machine
q = state
G = guard when to switch
R = reset update parameters as required

## Zeno phenomenom

- infinite switches in finite time
- type 1 zeno
  - happens when guard conditions are flipped
  - add a new intermediate state
  - Lie Derivative
  - g(x) == 0
  - is type 1 IF Lf1g < 0 AND Lf2g > 0
    - being pulled in different directions
    - fix with sliding mode
  - Lf1g is partial derivative of g with respect ot x
    - Lf1g -> dg/dt \* f1
    - Lf2g -> dg/dt \* f2
- q1
  - x_dot = 6 - x
  - guard x < 10
- q2
  - x_dot = 5x
  - guard x >= 10
- solution

  - time derivative of guard g(x) = 0 where x == 10 (combined switch point)
  - find where Lf1g is less than 0
    - Lf1g = 6 - x is less than 0 when x > 6 (pointing down)
  - find where Lf2g is greater than 0
    - Lf2g = 5x is greater than zero when x > 0 (pointing up)
  - if both are true, zeno effect is enbled
  - add sliding control
    - for each state
    - if zeno effect, go to new state x_dot = 1/(Lf2g - Lf1g) \* (Lf2gf1 - Lf1gf2)
      - in this state if g > 0 go back to q1
      - in this state if g < 0 go to state q2
    - otherwise go back and forth between original states
  - sliding mode dynamics
    - dynamics 1/(Lf2g - Lf1g) \* (Lf2gf1 - Lf1gf2)
    - set dg/dt == 0
    - g(x) = x - 10 (crossover point)
    - x_dot = 0
    - x = 0
    - solve both equations
    - f1 = 6-x
    - f2 = 5x
    - fill in the dynamics equations

- type 2 zeno
  - too hard
