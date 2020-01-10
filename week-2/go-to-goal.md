# GO TO GOAL CONTROLLER

e = phi_d - phi (use e')
w = PID(e)

x_g,y_g : goal
x,y : current position

desired angle phi_d
phi_d = atan(y_g-y,x_g-x)
use atan2 on angles

pure P controller
omega = K_big (phi_d' - phi')
