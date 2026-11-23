"""Read-only orientation observation. Candidate angle only; frame convention uncalibrated."""
import asyncio
import csv
import math
import time
import navel


async def main():
    async with navel.Robot() as robot:
        filename = "orientation_data.csv"
        print("Read-only orientation inspection. Candidate angle = atan2(y, x).")
        with open(filename, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["sample", "timestamp", "position_x", "position_y",
                        "orientation_x", "orientation_y", "orientation_z",
                        "orientation_w", "xy_magnitude", "candidate_angle_degrees"])
            for i in range(100):
                d = await robot.next_locomotion()
                p, o = d.odometry.position, d.odometry.orientation
                ox, oy = float(o.x), float(o.y)
                magnitude = math.hypot(ox, oy)
                angle = math.degrees(math.atan2(oy, ox))
                w.writerow([i, time.time(), float(p.x), float(p.y), ox, oy,
                            float(o.z), float(o.w), magnitude, angle])
                if i % 10 == 0:
                    print(f"{i:03d} pos=({p.x:.3f},{p.y:.3f}) angle={angle:.2f} deg |XY|={magnitude:.4f}")
                await asyncio.sleep(0.2)
        print(f"Finished. Saved {filename}")


if __name__ == "__main__":
    asyncio.run(main())
