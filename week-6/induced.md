# induced mode

- wall following
- use as induced mode
- alpha R(+=PI/2)u_ao

- x,xo,xg
- delta = ||x-xo|| distance from obstacle
- go to goal, compute vector towards goal
- avoid obstacles, compute vector away from obstacle
- switching surface

  - g(x) = 1/2(||x-xo||^2 - Δ^2) = 0
  - gtg : f1 , g > 0
  - ao : f2 , g < 0
  - f1 = Cgtg(xg-x)
  - f2 = Cao(x-xo)
  - induced mod3
    - dg/dx = (x - xo).T
    - x_dot = (1/(Lf2g - Lf1g)) \* (Lf2gf1 - Lf1gf2)
    - Lf1g = dg/dxf1 = Cgtg \* (x-xo).T @ (xg-x)) : inner product
    - Lf2g = dg/dxf2 = (x-xo).T \* Cao(x-xo) = Cao||x-xo||^2
    - Lf2g - Lf1g = (x-xo).T (Cao(x-xo)-Cgtg(xg-x))
    - Lf2f@f1 = Cao||x-xo||^2 @ (xg-x)) @ Cgtg(xg-x)
    - Lf1g@f2 = Cgtg \* (x-xo).T @ (xg-x)) @ Cao(x-xo)
    - ucFW = alphaR(-pi/2)u_ao
    - uccFw = alphaR(pi/2)u_ao
    - alpha and sign of pi/2 pops out of the indced mode
  - instead,
    - choose an alpha (1)
    - use inner product test to determine sign of pi/2

- if both vectors are colinear its hard to know which way to go!
