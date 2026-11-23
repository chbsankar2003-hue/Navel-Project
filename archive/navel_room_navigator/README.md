# Navel Room Navigator — safe first-stage project

This project is a **starter scaffold**, not a complete autonomous navigation system.
It is designed for the Navel robot SDK documented at https://doc.navelrobotics.com/.

## Safety
- Ask the lab supervisor to show the physical emergency stop before moving.
- Run `01_inspect_sensors.py` first. It does not command movement.
- Do not run movement scripts until the robot has clear space and a supervisor approves.
- Start with the robot on an open, level floor, people clear, and short distances.
- Software stop/cancel is not a substitute for the physical emergency stop.
- Do not use obstacle thresholds until the sensor values and units have been verified on this robot.

## Files
- `01_inspect_sensors.py`: prints Navel range-sensor readings and odometry. No movement.
- `02_short_move_test.py`: a supervised, short 0.20 m movement at low speed. No obstacle avoidance.
- `03_sensor_notes_template.md`: record sensor names, values, units, and physical measurements.
- `requirements-not-on-laptop.txt`: explains where the Navel SDK is expected to be.

## Where to run
Run the Python files **on the Navel robot** over SSH, or from a lab PC using SSH.
The robot's SDK (`navel`) is expected to be installed/configured on the robot. Do not assume it is installed on your home laptop.

## First run
1. Connect laptop/lab PC to the robot Wi-Fi.
2. SSH to the robot: `ssh navel@ROBOT_IP`
3. On the robot, create a project folder:
   `mkdir -p ~/control-studio/scripts/room_navigator`
4. Copy the files into that folder (see transfer instructions supplied separately).
5. Run:
   `python3 01_inspect_sensors.py`
6. Record readings in `03_sensor_notes_template.md`.
7. Only after sensor inspection and supervisor approval, run:
   `python3 02_short_move_test.py`

## Why there is no automatic obstacle-avoidance script yet
Navel documents `next_locomotion()` and range arrays:
- SONAR: front-right, front-left, back
- LIDAR: front, back

But your particular robot's availability, units, and range values must be checked first. This scaffold deliberately avoids guessing units or treating a missing/invalid sensor reading as clear space. After you share the sensor-inspection output, we can create the correct obstacle-aware controller for this robot.
