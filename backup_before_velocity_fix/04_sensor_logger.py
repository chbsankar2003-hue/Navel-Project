"""Read-only Navel sensor logger. Writes sensor_data.csv in the current directory."""
import asyncio
import csv
import time
from navel import NavelRobot


def find_group(distances, wanted):
    if not hasattr(distances, "items"):
        return []
    for key, values in distances.items():
        label = str(getattr(key, "value", key)).lower()
        if wanted in label:
            return list(values) if values is not None else []
    return []


def at(values, index):
    try:
        return float(values[index])
    except (IndexError, TypeError, ValueError):
        return None


async def main():
    robot = NavelRobot()
    filename = "sensor_data.csv"
    print(f"Read-only logging for 100 samples (~20 s). Output: {filename}")
    with open(filename, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["sample", "timestamp", "position_x", "position_y",
                    "heading_x", "heading_y", "velocity_x", "velocity_y",
                    "lidar_0", "lidar_1", "sonar_0", "sonar_1", "sonar_2"])
        for i in range(100):
            d = await robot.next_locomotion()
            p, o, v = d.odometry.position, d.odometry.orientation, d.odometry.velocity
            lidar = find_group(d.distances, "lidar")
            sonar = find_group(d.distances, "sonar")
            row = [i, time.time(), float(p.x), float(p.y), float(o.x), float(o.y),
                   float(v.x), float(v.y), at(lidar, 0), at(lidar, 1),
                   at(sonar, 0), at(sonar, 1), at(sonar, 2)]
            w.writerow(row)
            if i % 10 == 0:
                print(f"{i:3d}: pos=({p.x:.3f},{p.y:.3f}) lidar={lidar} sonar={sonar}")
            await asyncio.sleep(0.2)
    print(f"Finished. Saved {filename}")


if __name__ == "__main__":
    asyncio.run(main())
