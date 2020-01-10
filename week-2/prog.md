# programming assignment

+simian/+robot/quickbot.m
+simian/+robot/+dynamics/DifferentialDrive.m

- 32 ticks/rev
  +simian/+robot/+sensor/WheelEncoder.m
- ir sensors
- 4cm to 30cm

simulator

controller gets sensor info + position/orientation estimate
controller computes
linear and angular velocities
convert to left/right wheel speed
update estimate of position and orientation

supervisor
+simiam/+controller/+quickbot/QBSupervisor.m

controllers
+simiam/+controller/GoToAngle.m

## convert output (v,w) to left/right wheel velocities

uni_to_diff function

- R = radius
- L = wheelbase
- return vel_r,vel_l

## update odometry - estimate new position and orientation

gets ticks, current estimate, constants
compute x,y,theta differences
add deltas to current estimate
save as new estimate
save number of ticks

## sensors QuickBot.m get_ir_distances

sensors return voltage [0.4,2.75] range for distance from [4,30]cm range
12 bit 1.8v ADC values [200,1375] counts
use polyfit and polyval to convert raw IR values to distances from fitted data
