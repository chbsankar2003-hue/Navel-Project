"""Read-only odometry position tracker. Writes position_tracking.csv."""

import asyncio
import csv
import math
import time

import navel


SAMPLES = 150
PERIOD_S = 0.2
MOVEMENT_DEADBAND_M = 0.002


async def main():

    async with navel.Robot() as robot:

        previous = None
        start = None
        total_distance = 0.0
        filename = "position_tracking.csv"

        print("Read-only position tracking.")
        print("No movement commands will be sent.")

        with open(filename, "w", newline="") as f:

            w = csv.writer(f)

            w.writerow([
                "sample",
                "timestamp",
                "position_x",
                "position_y",
                "delta_x",
                "delta_y",
                "step_distance",
                "displacement",
                "total_distance",
                "orientation_x",
                "orientation_y",
                "orientation_z",
                "orientation_w"
            ])

            for i in range(SAMPLES):

                d = await robot.next_locomotion()

                od = d.odometry

                p = od.position
                o = od.orientation

                x = float(p.x)
                y = float(p.y)

                if start is None:
                    start = (x, y)

                if previous is None:

                    dx = 0.0
                    dy = 0.0
                    step = 0.0

                else:

                    dx = x - previous[0]
                    dy = y - previous[1]

                    step = math.hypot(dx, dy)

                    if step > MOVEMENT_DEADBAND_M:
                        total_distance += step

                displacement = math.hypot(
                    x - start[0],
                    y - start[1]
                )

                w.writerow([
                    i,
                    time.time(),
                    x,
                    y,
                    dx,
                    dy,
                    step,
                    displacement,
                    total_distance,
                    float(o.x),
                    float(o.y),
                    float(o.z),
                    float(o.w)
                ])

                if i % 10 == 0:

                    print(
                        f"{i:03d} "
                        f"pos=({x:.3f},{y:.3f}) "
                        f"displacement={displacement:.3f}m "
                        f"total={total_distance:.3f}m"
                    )

                previous = (x, y)

                await asyncio.sleep(PERIOD_S)

        print("\nFinished.")
        print("Saved:", filename)

        print(
            f"Final displacement: {displacement:.3f} m"
        )

        print(
            f"Estimated path length: {total_distance:.3f} m"
        )


if __name__ == "__main__":
    asyncio.run(main())
