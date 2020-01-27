# sliding mode control

- Type 1 Xeno system

  - f1 { -1 x >= 0}
  - f2 { 1 x < 0>}
  - chatters at x == 0

- switching surface

  - g(x) == 0
  - both vectors point inwards 'bad'
  - should slide along the switching surface

- sliding
  - f1 point negative
  - f2 point positive
  - gradient (dg_t/dx).T (partial derivatiex)
  - dg/dx \* f2
    - if positive, f2 vector is in same direction
  - dg/dx \* f1
    - if negative , pointing in different directions
  - sliding occurs if
    - dg/dx*f1 < - and dgdx*f2 > 0
    - derivative of g in direction f = Lfg = Lie derivative
  - this tests for type 1
  - what happens beyond the Zeno point?
    - don't know yet
