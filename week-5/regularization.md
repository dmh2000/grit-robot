# Regularization

if sliding occurs, what to do?

- g = 0
- dg/dt = 0
- dg/dt = dg/dx \* x_dot ->
- dg/dx \* (sigma1f1 + sigma2f2) =
- sigma1* Lf1 * g + sigma2 \* Lf2g
- Lf1,Lf2 -> Lie derivative
- needs to be == 0
- can then solve for sigma2 or sigma2
- sigma1,sigma2 >= 0
- sigma1 + sigma2 = 1

- example

  - f1 { -1 x >= 0}
  - f2 { +1 x < 0>}
  - switching surface = g(x) = x = 0
  - Lf1g = dg/dx \* f1 = 1 \* -1 = -1
  - Lf2g = dg/dx \* f2 = 1 \* 1 = +1
  - sigma2 = -sigma1(Lf1g/Lf2g) = -sigma1(-1/1) = sigma1
  - sigma1 == sigma2
  - sigma1 == sigma2 = 0.5
  - induced mode
  - x_dot = 0.5f1 + 0.5f2 = 0

- Induced Mode add a state
  - I can compute sigma 1 and 2
  - x_dot = (1/(lf2g - lf1g))(Lf2gf1 - Lf1gf2)
  - if g == 0 and sliding condition

Summary

- models
- stability awareness
- Zeno conditions
- Regularizations
