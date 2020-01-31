# practical considerations

- noisy sensors

- non-point obstacles
  - obstacles aren't points
- fat guards
  - never exactly delta
  - delta += epsilon
- tweak...

  - deltas
  - epsilons
  - C's

- non-point obstacles

  - sensors return points
  - options
    - use closest
    - good : weigh and add obs vectors depending on distance
    - better : weigh and add depending on distance and direction of travel
    - best : make a map and plan (no in this class)

- fat guards
  - g(x) < 0 - ε
  - g(x) > 0 + ε
  - ε creates a corridor
