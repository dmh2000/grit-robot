# Practical Considerations

- separation principle means we can decouple control and observer design (in theory)
- the controller is only useful until state estimate is close
  - observer should converge faster than controller
  - observer can have large eigenvalues
  - observer is software, will not saturate

## Humanoid Robot

- theta_dot_dot = 1/J(Ki - btheta_dot)
  - theta = angle of joint
  - J = moment of interation
  - K = torque constant (current -> acceleration)
  - i = current (input) = u
  - b = friction coefficient

put in state space form

- x1 = theta
- x2 = theta_dot
- y = theta
- A = [[0,2],[0,-b/J]]
- B = [0,K/J]
  x_dot = [[0,1],[0,-b/J]] @ x + [0,K/J]u
  y = [1,0] @ x

## reference tracking

system dynamics

- e = [theta - theta_d,theta_dot]
- e_dot = Ax + Bu -> [theta_dot,theta_dot_dot]
- e_dot = Ae + A[theta_d,0] + BU
- e_dot = Ae + Bu
- y = Cx = Ce + C[theta_d,0] = Ce + theta_d

plug into standard controller
u = -Ke_hat
e_hat_dot = Ae_hat + Bu + L(y - Ce_hat - theta_d)

## beyond pole placement

- u = -Kx_hat
- x_hat_dot = Ax_hat + Bu + L(y-cx_hat)
- LQ Optimal COntrol
- Kalman Filter
- real world is more complex than simple LTI systems
- Hybrid Systems
