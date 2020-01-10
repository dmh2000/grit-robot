# control design basics

car model:
x_dot = (c/m) \* u

want x such that:
x -> r as t -> infinity
e = r - x goes to zero

## attempt 1: bang-bang control

- +u_max if e > 0
- -u_max if e < 0
- 0 if e = 0
- overreacts to small errors
- large oscillations in control output
- jerky
- burn out actuators

## attempt 2: P regulator

- e = r - x
- u = k \* e
- stable
- add wind resistance
- x_dot = (c / m) \* u - gamma\*x
- at steady state, x does not change
- time derivative of x is 0
- x is always less than r

## performance objectives

- stability (bounded-in, bounded out) BIBO
- tracking
- robustness

## attempt 3: P with wind resistance term

- u = k \* e + gamma \* (m/c) \* x
- not robust, don't know gamma, m, c

## attempt 4 : PI regulator

- take integral over error
- u = k \* e
- u(t) = k_p \* e(t) + k_i \* integral e(tau)d(tau)
- k_p : proportional gain
- k_i : integrator gain

## attempt 5 : PID regulator

u(t) = k_p \* e + k_i \* integral(e) + k_d \* derivative(e)
