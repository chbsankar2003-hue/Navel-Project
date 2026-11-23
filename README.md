# Navel Project — Room 223 Environment Tracking & Navigation

This repository contains a staged, safety-first implementation for the Navel robot.

## Current status
- Initial sensor inspection, CSV logging, odometry observation, position tracking and heading observation have been performed in the lab.
- LiDAR response to controlled obstacle distances is **not yet validated**.
- Sonar has repeatedly returned zero in the observations so far; do not interpret zero as a clear path.
- The heading estimate `atan2(orientation.y, orientation.x)` is a candidate derived from observed data, not yet a fully calibrated room-frame heading.

## Important safety rules
1. These scripts are read-only: they do not command robot motion.
2. Do not add autonomous movement until sensor behaviour, stop behaviour and emergency stopping have been tested.
3. Keep a person at the robot and keep a clear stop route during any later motion test.
4. Do not commit passwords, Wi-Fi credentials, API keys, SSH private keys, or personal data.
5. Keep raw experiment CSV files locally unless you deliberately decide they are suitable for the repository.

## Repository structure
- `scripts/`: read-only sensor and odometry experiments.
- `docs/`: experiment notes and development plan.
- `data/README.md`: where to store local CSV output (CSV files are ignored by Git by default).

## Run on the robot
The Navel Python SDK is installed on the robot. Run these scripts in the robot's Python environment, from the project folder. The laptop is for editing and version control.

Example:
```bash
python3 scripts/01_inspect_sensors.py
python3 scripts/10_lidar_validation.py
```

If the `navel` Python package is not available on the laptop, that is expected. Do not install random packages to imitate the robot SDK.

## Git workflow
On your personal laptop:
```bash
git status
git add README.md docs scripts .gitignore data/README.md
git commit -m "Add initial Navel sensor and odometry experiments"
git push
```

On the lab PC, inside the existing project checkout:
```bash
git status
git pull
```
If the lab PC does not have a clone yet, use the setup instructions in `docs/GIT_WORKFLOW.md`.

## Important note about historical scripts
This starter pack reconstructs clean, documented versions of the experiments from the information currently available. It may not be byte-for-byte identical to the files previously created in the lab. Preserve your original lab scripts and CSV files; compare before replacing anything.
