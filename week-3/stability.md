# stability

- stability most important feature of controller
- tracking
- robustness
- other

## scalar

x_dot - ax -> x(t) e^at \* x(0)

- unstable
  - if a > 0 will eventually blow up
  - any initial condition blows up
- asymptotically stable
  - if a < 0 will eventually go to zero
  - all initial conditition where a goes to 0
- critical stability
  - if a == 0 x doesn't change
  - doesn't blow up
  - doesn't go to 0

x_dot = Ax -> x(t) => e^At \* x(0)
find eigenvalues of A

if Av = lambda \* v -> lambda is an eigenvalue
lambda is complex
v is an eigenvector ->R
'eig' function to get eigenvalues
stable if eigenvalues are negative
eigenvector tells what happens along dimensions

## matrix

A = [
1,0
0,1
]
eig(A) = 1,-1
v = [1,0], v2 = [0,1]

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

**want to design for asymptotic stability**

- compute eigenvalues of A matrix
- if all real parts are negative

pendulum 1

- A = [[0,1],[-1,0]] lambda 1 = j, lambda 2 = -j
  - critically stable, will oscillate forever
- A = [[0,1],[1,0]] lambda 1 = -1, lambda 2= 1
  - unstable
