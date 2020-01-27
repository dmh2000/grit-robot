# Danger Beware

Stable subsytems do no guarantee a stable hybrid system

- ignoring resets, we can write the hybrid system as a switched system
  - x_dot = f_sigma(x,u)
  - sigma is the switch signal

## different kinds of stabily

- universal asymptotic stability
  - x -> 0 no matter how it switches
  - all sigma
- existential asymptotic stability
  - x -> 0 for some switch logic but not all
  - some sigma where x -> 0
- hybrid asymptotic stability
  - x -> 0

## results

- if all individual modes are A.S?, then
  - it will be existentially stable
    - example: stay in one mode
  - no always universally A.S
- what to do?
  - find common Lyapunov function (hard)
  - never design unstable controllers
  - test,test,test
