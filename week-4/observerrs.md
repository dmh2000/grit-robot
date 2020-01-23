# OBSERVERS

- we don't have x
- we only have y
- u in, y out
- take y, push it through a block, get estimate x_hat of state out
- x_hat is an observer

Predictor-Corrector
Luenberger observer

- x_dot = Ax
- y = Cx
- Predictor
  - make a copy of the system
  - x_hat_dot = Ax_hat
- Corrector
  - add a notion of how wrong the estimate is
  - x_hat_dot = Ax_hat + L(y - Cx_hat)
  - L(y - Cx_hat) = difference between y and y estimate
- what is L?
  - define estimation error e as difference bewtween actual and esimate
  - e = x - x_hat
  - make e asymptotically stable
  - e_dot = x_dot - x_hat_dot = Ax - Ax_hat - L(y-Cx_hat)
  - e_dot = A(x-x_hat) - LC(x - x_hat) = (A - LC)e : dynamics of estimation error
  - pick L such that eigenvalues of A-LC have negative real part
  - use pole placment
  - e_dot = (A - LC)e
  - want : Re(eigh(A-LC)) < 0
  -

## does this always work?

- no, doesn't always work
- is y (sensor suite) rich enough for observability
