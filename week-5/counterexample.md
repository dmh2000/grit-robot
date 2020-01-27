# Counter Example

## two mode system

- x_dot = A1x
  - [[-e,1],[-2,-e]]x
- x_dot = A2x
  - [[-e,2],[-1,-e]]x
- eig(A_i) = -e +- 1.41i
- both asymptotically stable
- has imaginary component, will oscillate
- switch between a1 and a2
  - a1 : x2 == 0
  - a2 : x1 == 0
  - stable, converges faster
- switch between a1 and a2
  - a1 : x1 == 0
  - a2 : x2 == 0
  - unstable, diverges

a hybrid system with stable modes may not be overall stable
