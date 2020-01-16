# swarm robotics

lambda = eigenvalue

- asymtotically stable
  - if and only if
    - real(lambda) < 0 for all eigenvalues of A
- unstable
  - if any eigenvalue is positive
- critically stable
  - only if
    - all real eigenvalues <= 0
    - one eigenvalue is 0 and rest have negative real part
    - or two purely imaginary eigenvalues and the rest have real part

## rendezvous problem

- given a collection of mobile agents who can only measure relative displacement of neighbors
- d = x_1 - x_2
- have all agents meet at the same unspecified point

- scalar case

  - u1 = x2-x1
  - u2 = x1-x2
  - x_dot = [[-1,1],[1,-1]] \* x
    - eigenvalues
    - 0,-2
    - no unstable
    - critically stable

- if one eigenvalue is 0 and all other negative real,

  - state ends up in null-space of A
  - null(A) = {x : Ax = 0}
  - scipy.linalg.null_space(A) = vector [alpha,alpha]
  - means alpha can be any real number
  - x1 -> alpha, x2 -> alpha, (x1 - x2) => 0
  - rendezvous is achieved
  - if more than two agents , they should aim a centroid of all the visible agents

- x_dot = sum(x_j - x_i) : consensus equation (all elements will agree)
- x_dot = -Lx (L = matrix Laplacian)
- if underlying graphi is connected then the graph Laplacian L has one zero eignvalue and rest are positive
- it is critically stable, goes to null space of L

2 kheperas
same pid go-to-goal controller as before
high level controllers pick imtermediary goal-points
robots keep track of position using odometry
positions are communicated rather then sensed
