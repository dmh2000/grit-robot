# programming and sim

- Blending
  - blend both in one
- Hard switching
  - switch between each
- Intermediary
  - blend the two when transitioning

## Blending

- compute gtg vector
- compute obstacle vector
- u_blend = alpha\*obs + (1-alpha)\*gtg
- 0 <= alpha <= 1
- u_ao = u_a0 / ||u_ao|| : normalized vector unit length
- u_gtg = u_gtg / ||u_gtg||

## hard switching

- if no objstacle use GTG vector
- if close to objstacle use OA vector

## intermediary

- avoid chattering by using blended between gtg and ao

## supervisor

- each controller is its own state
- supervisor can switch controllers
- obj.switch_to_state('stop'); // collision
- obj.check_event('at_goal') // within obj.d_goal of the goal location
-
