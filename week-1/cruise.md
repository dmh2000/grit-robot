# cruise control

make a car drive at desired reference speed 'r'
newtons second law : f = ma

state : velocity : x (speed of car)
x = velocity
a = dv/dt = derivative of velocity
input :

- f = cu
- u : gas/brake
- c : coefficient of electro-mechanical system

F = ma
F = cu
ma = cu
a = cu / m
x_dot = (c / m) \* u

### control design

- assume we can measure the velocity
  - y = x
- the control signam shoudl be a function
  - e = r-y (error)
- minimize error

### properties of useful controller

- small e gives small u, don't overreact
- u should not be jerky
- u should not depend on knowing c and m exactly
