# OBSTACLE AVOIDANCE CONTROLLER

- interpet ir distance to a point in robot coordinate frame
- transfor this point from robot frame to world frame
- compute vector that points away from obstacles

coordinate frame transforms

- world frame centered at origin (0,0)
- robot is at (x,y,theta)
- theta is orientation with respect to x axis counter clockwise
- sensor coordinates are in robot frame (centered at robot with robot orientation
- sensor #1 robot frame located at (x_s1,u_s1,theta_s1)
- sensor #1 world frame orientation theta' = 90 + theta
- sensor coordinate frame origin at sensor location (x,y,theta)
  - point in sensor coordinates = (distance,0)

world frame -> robot frame
robot frame -> world frame
sensor frame -> robot frame

2d rotation/translation
p = (1,0,0) -> R(1,2,pi/4)
R is transform matrix
takes a vector v
R = [
[cos,-sin,x],
[sin,cos,y],
[0,0,1]
]
p = [x,y]
o = theta]

sensor -> world
w = robot-world @ sensor-robot @ [d,0,1]
w = R(x,y,theta) @ R(x_s,y_s,theta_s) @ [d,0,1]

matlab
compute world frame coordinates of sensed points
sum the vectors
results in direction and magnitude away from close obstacles
