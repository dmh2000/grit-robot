# POLE PLACEMENT

Pick control gains such that the eigenvalues (poles) of the closed loop
system match the desired eigenvalues

XA - BK(L) = L^2 + an-1L^n1 + ... a1L + a0
det(LI - (A - BK))
chi(L) = prod(L-li) = L^2 + bn-1L^n1 + ... b1L + b0
an-1(K) = bn-1
...
a0(K) = b0

- is it possible?
  - (NO)
- how do we pick eigenvalues
  - mix of art and science
- computing large determinants
  - NO
  - in matlab
  - p = [l1,l2,...]
  - K = place(A,B,P)

Controlability

- is pole placement possible
- smallest eigenvalue dominates convergence
- if smallest is large,
  - might saturate actuators
- complex-conjugate pair
  - R,+-i
