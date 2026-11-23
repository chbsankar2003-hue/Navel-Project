"""Read-only LiDAR validation logger. Run one capture per obstacle placement."""
import asyncio
import csv
import time
from statistics import median
import navel

SAMPLES = 50
PERIOD_S = 0.2


def lidar_values(distances):
    if hasattr(distances, "items"):
        for key, values in distances.items():
            if "lidar" in str(getattr(key, "value", key)).lower():
                return list(values) if values is not None else []
    return []


async def main():
    async with navel.Robot() as robot:
        label = input("Enter placement label (e.g. near, middle, far, no_obstacle): ").strip()
        if not label:
            label = "unspecified"
        filename = f"lidar_validation_{label}.csv"
        first_values, second_values = [], []
        print("Keep the robot stationary. Do not move it during this 10-second capture.")
        print("This script only records; it does not command motion.")
        with open(filename, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["sample", "timestamp", "placement_label", "lidar_0", "lidar_1"])
            for i in range(SAMPLES):
                d = await robot.next_locomotion()
                vals = lidar_values(d.distances)
                a = b = None
                try:
                    a = float(vals[0])
                    if a <= 0: a = None
                except (IndexError, TypeError, ValueError):
                    pass
                try:
                    b = float(vals[1])
                    if b <= 0: b = None
                except (IndexError, TypeError, ValueError):
                    pass
                if a is not None: first_values.append(a)
                if b is not None: second_values.append(b)
                w.writerow([i, time.time(), label, a, b])
                if i % 10 == 0:
                    print(f"{i:02d}: LiDAR[0]={a} LiDAR[1]={b}")
                await asyncio.sleep(PERIOD_S)
        print(f"\nSaved: {filename}")
        print("Median LiDAR[0]:", median(first_values) if first_values else "NO VALID DATA")
        print("Median LiDAR[1]:", median(second_values) if second_values else "NO VALID DATA")
        print("Compare medians across placements. This is not metric calibration unless distances are measured.")


if __name__ == "__main__":
    asyncio.run(main())
