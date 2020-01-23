# SEPARATION PRINCIPLE

we have building blocks

- Controllability
- Observability
- State Feedback
- Observers
- Pole Placment

## separation principle

- put everything together
- couple control and observers

- linear time invariant system
- x_dot = Ax + Bu
- y = Cx
- assume CC and CO
- if not CC, buy better actuators
- if not CO, buy better sensors

### design state feedback controller as if we had x

- u = -Kx => x_dot = (A-BK)x (design for)
- u = -Kx_hat (actually have)

### estimate x using an observer

- observer needs u also

### analyze joint dynamics

- x_dot = Ax - BKx_hat = (A-BK)x + BKe
- e = (A - LC)e
- [x_dot,e_dot] = [[A-BK,BK],[0,A-LC}]]@[x,e]
- it is a upper triangular block matrix
- eigenvalues are given by the diagonal blocks
- A-BK, A-LC (ignore BK)
- but we already have eigenvalues for those terms

## SEPARATION PRINCIPLE DEFINITION

- can design controllers as if we have x
- can design observers independent of control actions
- control and observer designs are separated

- PLANT (dynamics of system)
  - x_dot = Ax + Bu
  - y = Cx
- CONTROLLER
  - x_dot = Ax_hat + Bu + L(y - Cx_hat)
  - u = -Kx_hat
