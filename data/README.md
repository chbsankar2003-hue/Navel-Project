# Experiment data

Keep raw CSV experiment outputs here locally. CSV files are ignored by Git to avoid accidentally publishing raw lab data or large logs.

For reproducible results, record:
- date and time
- script name and Git commit
- robot position/orientation setup
- obstacle material and approximate relative placement
- whether the robot was stationary
- any anomalies or interruptions

If you later want to publish selected anonymised results, explicitly remove `*.csv` from `.gitignore` for the chosen file and review it before committing.
