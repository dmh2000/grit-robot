# odometry

need to know where robot is
state
x,y,phi

how to obtain state information

- external sensors
  - ultrasound
  - infrared
  - lidar
  - radar
  - gps
- internal sensors
  - imu
    - acceleromters
    - gyros
  - orientation : compass
  - encoders
    - tick counts of turning wheels

## wheel encoders

- R : radius
- L : wheelbase (width)
- distance moved by each wheel
- assume wheels are following an arc
  - constant rate
  - constant velocity
  -
- encoder ticks

for both wheels
N = number of ticks per revolution
delta_tick = tick_now - tick_old
D_wheel = 2phiR(delta_tick / N)

- D_l : 2piR(dtick_left/N)
- D_r : 2piR(dtick_right/N)
- D_c : (D_l + D_r) / 2 (center)

' -> new value
x' = x + D_c \* cos(phi)
y' = y + D_C \* sin(phi)
phi' = phi + (D_r - D_l)/L

## Drift

Odometry drifts!
wheel spin
