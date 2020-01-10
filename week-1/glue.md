# GLUE lecture

## dynamical models

using dynamic model - description of how system changes with time
exponential increase

t_0 = 0
x_0 = 10

## continuous

- x(t) = x_0 \* e^(2(t-t0))
- x_dot(t) = 2 \* x_o \* e^(2(t-t0))
  - = 2 \* x(t)
- x_dot_dot(t) = 4 \* x_o \* e^(2(t-t0))
  - = 4 \* x(t)

## initial conditions

t_0 = 0
x_0 = 10

- t = 0
  - x(t) = 10e^2t

## using differential equation

- x_dot(t) = 2x (continuous time)
- x(0) = 10
- dt = 0.5
- k is a counter
- t = k \* dt
- taylor expansion
- first two terms -> linear approximation
  - x_1 = x_k + dt\*x_dot + (dt^2/2!)\*x_dot_dot_k
- x_dot(t) = 2x
- dt = 0.5
- t = k \* dt
- simplify
  - x_k1 = x_k + dt \* 2x_k
  - x_k1 = x_k + (0.5 \* 2)x_k
  - x_k1 = x_k + x_k
  - x_k1 = 2x_k

x_dot(t) = f(x,t)
x(t*) = x*

## to get continuous equation x(t), integrate

- x(t) = x_0 \* e^2(t-t0)

## candidate model

- x_dot(t) = 2x
- x(0) = 10
- x(t) = 10e^2t
- initial condition check
  - eval model at initial condition should be correct
- differential equation check
  - take derivative of candidate differential equation for x(t)
  - should match model

x_dot(t) = 9x + 3  
x(3) = 5
x(t) = 16/3 \* e^9(t-3) - 1/3

- solve numerically
- analytically
- check candidate solution
  - initial condition
    - plugin x(3) to x(t)
    - 16/3 \* 1 - 1/3 = 15/3 = 5
  - differential equation

## Equalibrium point

if x wakes up at x, it stays there
x_dot(t) = 0
