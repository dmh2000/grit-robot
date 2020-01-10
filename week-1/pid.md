# PID Controller

## performance objectives

- stability (bounded-in, bounded out) BIBO
- tracking
- robustness

## gains:

- k_p : medium rate response
  - stability, medium rate responsiveness
- k_i : slow rate response
  - tracking
  - disturbance rejection
  - large k_i causes oscillations
- k_d : fast rate response
  - sensitive to noise

## PID :

- stability is not guaranteed
- feedback fights undertainty in model parameters

## cruise control

x_dot = (c/m) \* u - gamma \* x
c = 1
m = 1
gamma = 0.1
r = 1

P: doesn't reach target

- k_p = 1
- k_i = 0
- k_d = 0

PI: large k_i may cause oscillation

- k_p = 1
- k_i = 1
- k_d = 0

PID:

- k_p = 1
- k_i = 1
- k_d = 0.1
