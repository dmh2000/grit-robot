# stabilizing the point mass

systematic control design

we don't know x (current state)
we only know y (output)

game plan:

- design u as if we had x
- figure out x from y

- step 1 : pole placement

  - u = -Kx = -[k1,k2]x
    - k1 position
    - k2 velocity
    - how to pick gains
    - pick K so the closed loop system has desired eigenvalues
      - negative real part
      - on unit circle

- given a matrix M, its eignevalues satisfy the characteristic equation

  - chi@M(lambda) = det(lambda@I - M) = 0
  - M = [[m1,m2],[m3,m4]]
  - lambda I - M = lambda [[1,0],[0,1]] - M = [[L-M1,-m2],[-m3,L-m4]]
  - take determinant of result
  - det(LI-M) = (L-m1)(L-M4) - m2m3
  - set determinant = 0
  - L^2 - (m1 + m2)L + m1m4 - m2m3 = 0
  - solve for L (the easy way)

- fundamental theorem of algebra

  - the roots in a polynomial are completely determined by the coefficients
  - L^2 - (m1 + m2)L + (m1m4 - m2m3) = 0

  ***

  - manipulate the coefficients
  - u = -Kx => x_dot = (A - BK)x (closed loop dynamics)
  - A - BK = [[0,1],[0,0]] - [0,1]@[k1,k2] = [[0,1],[-k1,-k2]]
  -

- XA - BK(L) = det([L,-1],[k1,L+k2]) = L^2 + Lk2 + k1
-              LI - (A-BK)L

- pick eigenvalues that we want
- l1...Ln (eigenvalues)
- characteristic equation(L) = (L-l1)(L-l2)...(L-ln) = prod(L-li)
- for the robot pick both eigenvalues at -1
- c(lambda) = (L+1)(L+1) = L^2 + 2L + 1
- line up the coeffciencts
- c(lambda) = (L+1)(L+1) = L^2 + 2L + 1
- c(lambda) = (L+1)(L+1) = L^2 + kL + k1
- k2 = 2
- k1 = 1
- K = [1,2]
