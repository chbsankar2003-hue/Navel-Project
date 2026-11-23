# Project plan

## Goal
Develop an incremental environment-tracking and navigation implementation for Navel in Room 223.

## Completed preliminary work
- Read LiDAR, sonar and odometry packets.
- Logged sensor observations to CSV.
- Built an initial threshold-based obstacle classifier.
- Observed odometry position and velocity while manually moving the robot.
- Estimated displacement and accumulated path length from successive positions.
- Observed orientation X/Y behaviour and candidate heading using `atan2(y, x)`.

## Known limitations
- LiDAR readings have not yet been validated against controlled obstacle positions.
- Sonar values have repeatedly been zero; zero is treated as unavailable, not free space.
- Heading direction is empirically observed but room-axis alignment and angle convention need calibration.
- Odometry path length is an estimate, not ground-truth measurement.
- No room dimensions or metric map have been established.

## Next lab sessions
1. Controlled LiDAR response test with robot fixed in one pose and a broad, matte obstacle placed at several relative distances/positions. No tape measure is essential for the first qualitative test; keep the placements repeatable and note them as near/middle/far. Do not claim metric calibration without measured distances.
2. Verify which LiDAR element corresponds to which physical direction and whether the readings respond consistently.
3. Plot position/heading and sensor readings over time; inspect odometry drift and heading wrap.
4. Only after sensor validation, create a simple local obstacle representation. Begin with sensor-relative observations, not a falsely precise full-room map.
5. Build a grid/map from repeatable observations and mark unknown cells as unknown, not free.
6. Implement start/goal selection and offline path planning (e.g. A*) on a verified map.
7. Test supervised low-speed motion and obstacle-stop behaviour before any autonomous navigation.

## Acceptance checks before movement automation
- Sensor readings respond predictably to an obstacle entering/leaving the validated sensing region.
- Invalid/zero readings never become "clear".
- Position and heading updates are stable enough for the intended test.
- A manual stop/emergency stop procedure is confirmed.
- First movement test is short, slow, supervised and in a clear area.
