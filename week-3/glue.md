# WEEK 3 GLUE

## Systems

- show how input and outputs define a system
- get used to matrices via two exmaples
  - second order in state space
  - linearization example

## what is a system

inputs to something that produces output

second order system : differential equation
m,f_dot_dot = alpha F_dot + beta f + cp =>
f(0) = initial condition

- x_dot = Ax + Bu
- y = Cx
- u -> (A,B,C) -> y

1. pick state variables and define inputs and output
2. write the second order differential equation as a pair of first order ones
3. put in terms of state,input,output

rewrite ODE in state space form:
x = [x1:f,x2:f_dot]
u = p (as in + cp)
y = f (or f_dot)

f_dot = x_dot_1 = x2
f_dot_dot = x_dot_2 = 1/m(alpha x2:f_dot + beta x1:f + cu)

- substitute
  - u for 'p'
  - x2 for f_dot
  - x1 for f

state
x_dot = [x1_dot,x2_dot]
A = alpha/m \* x2 + beta/m \* x2
A = [[0, 1],[b/m, a/m]] @ state
B = [[0,c/m]] @ u

## linearize around x = 0

z_dot_dot = lz_l^2 + g z_dot + c tau
