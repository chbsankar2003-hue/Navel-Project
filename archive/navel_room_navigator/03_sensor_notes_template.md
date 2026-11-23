# Navel sensor inspection notes

Robot / asset number:
Date:
Room:
Operator / supervisor:

## Sensor readings
Run `01_inspect_sensors.py` while robot is stationary.

| SDK sensor key | Documented placement/order | Raw values observed | Confirmed unit | Physical measurement |
|---|---|---|---|---|
| SONAR | front-right, front-left, back | | | |
| LIDAR | front, back | | | |

## Calibration experiment
For each sensor:
1. Place a flat obstacle at a measured distance (supervisor-approved).
2. Record the raw sensor value.
3. Repeat at several distances.
4. Determine whether the values are meters, millimeters, or another representation.
5. Note `None`, zero, negative, or out-of-range readings.
6. Do not use an unverified reading for motion control.

## Odometry
Position:
Orientation:
Velocity:
Does it update while stationary?
Does it update after the supervised short movement?

## Safe obstacle threshold (only after verification)
Chosen threshold:
Reason:
Sensor(s) used:
What happens if a sensor is missing/invalid:
Supervisor approval:
