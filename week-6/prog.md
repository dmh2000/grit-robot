# programming

Wall Following

- add another controller
- estimate section of wall as a vector
  - perpendicular, tangential
  - combine two vectors
  - steer in that direction
- follow left
  - calculate tangential vector 'u_fw_tp'
    - use sensors 1,2,3
    - pick shortest two
    - convert points to world frame
    - compute tangential vector 'u_fwd_tp' [p2-p1]
  - calculate perpendicular vector 'u_fw_p'
    - pick sensor 1 point 'u_a'
    - convert to world frame
    - get robot world frame position 'u_p'
    - compute vector from robot to wall
    - u_fw_p = (u_a = u_p) - ((u_a-u_p) @ u_fwd)u_fw_t
  - calculate vector away from wall
    - -d_fw (u_fw_p/norm(u_fw_p))
    - d = distance desired from wall
  - u_fw
    - combine two vectors
    - u_fw = alpha u_fw_tp + beta u_fw_p
    - steer in direction of u_fw
- follow right
  - use sensors 3,4,5
  -
