# SENSORS

abstract what the various sensors do

## range sensor skirt

- ultrasound
- IR
- LIDAR

## other sensors

- vision
- tactile
- gps

## Disk Abstraction

- assume know distance and direction of obstacles
- assume a disc around the robot based on sensor range
- obstacles
  - d : distance
  - phi : angle relative to robot heading
  - global position
    - x_obs = x + d_obs cos(phi_obs + phi)
    - y_obs = x + d_obs sin(phi_obs + phi)

## Rendevous Problem , multiple robots

- each robot aims at cg of other robots detected by range sensor skirt
