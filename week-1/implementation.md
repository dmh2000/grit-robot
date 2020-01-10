# implemntation

## PID regulator

u(t) = k_p \* e + k_i \* integral(e) + k_d \* derivative(e)

sample_time : delta_t

## derivative term:

store old error
(e_new - e_old) / dt

## integral term

accumulate error
sum of errors = E
E_new = E_old + e

- read e
- e_dot = (e_new-e_old)/ dt
- E_new = E_old + e
- integral is dt /\* E_new

## implemntation

- read e
- e_dot = (e - e_old)/ dt
- maybe extract dt into k_d if dt is known
- E = E + e
- u = k*p /* e + k*d * e_dot + k_i \* E
- old_e = e

## quadrotor height control

- x_dot_dot = c \* u - g
- control velocity of controller collective
- u = k_p _ e + k_i _ E + k_d \* e_dot
-
