# 1.2 building blocks

- state : representation of what the system is currently doing
  - x
- dynamics : description of how the state changes over time
- reference: what we want the system to do
  - r
- output : measurement of some aspects of the system
  - y
- input : control signal
  - u
- error : r - y

feedback loop
r --+--> u -> x --+--> y
^ |
|-------------|

robot :
inputs : velocity, acceleration
measurement : where, how fast

# 1.3 models

how to pick input control signal

## objectives

- stability (most important)
- tracking
  - given a reference, how to move to it
- robustness
  - immunity to model parameters
- disturbance rejection
- optimality

  - how to do it 'best'

effective control strategies rely on predictive models
discrete time:

- x_k+1 = f(x_k,uk) difference equation
- how to go from k to k+1
- clock
  - x_k+1 = x_k + 1

continuous time:

- no notion of 'next'
- derivatives : change with respect to time
- differential equations
- x_dot = f(x,y)
- clock
  - x_dot = 1

continuous to discrete:

- x_dot = f(x,y)
- sample time delta_t
- x_k_1 = x(k\*delta_t) => x((k+1)dt)
- f = ma
- x(k*dt + dt) ~ x(k*dt) + dt*x_dot(k*dt)
- x_k_1 = x_k + dt \* f(x_k,u_k)
