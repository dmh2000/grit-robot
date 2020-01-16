# LTI Systems

1. ignore input and output

no input
x_dot = Ax
x(t0) = x0

what is the solution
scalar version
x_dot = ax, x(t0) = x0 , solution => x(t) = e^(a(t-t0)x0

- plug in initial conditions
  - x0 = e^a(t0-t0)\*x0 = e^0\*x0 = 1\*x0
- check that solution (integral of x_dot = ax)
  - take time derivative of solution and plug in initial condition
  - verify it results in the intial ODE
  - dx/dt:(t) = ae^a(t-t0)x0 = ax

for higher order systems, get a matrix version
just like scalar version
d/dt e^At = Ae^(At)

e^A(t-t0) = PHI(t,t0) => State Transition matrix

x_dot = Ax => x(t) = PHI(t,tau)x(tau)

**controlled system**
x(t) = PHI(t,t0)x(t0) + integral(t0,t) PHI(t,tau)Bu(tau)dtau
