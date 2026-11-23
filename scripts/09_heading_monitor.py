"""Read-only heading monitor. Net rotation is relative to initial heading."""
import asyncio
import csv
import math
import time
import navel


async def main():
    async with navel.Robot() as robot:
        previous_raw = None
        unwrapped = None
        initial_unwrapped = None
        total_absolute_turn = 0.0
        start_time = time.time()
        filename = "heading_monitor.csv"
        print("Read-only. Test manual left/right rotation with the robot safely clear.")
        with open(filename, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["elapsed_time", "position_x", "position_y",
                        "heading_degrees", "heading_change_degrees",
                        "net_rotation_degrees", "total_absolute_turn_degrees"])
            for i in range(150):
                d = await robot.next_locomotion()
                p, o = d.odometry.position, d.odometry.orientation
                raw = math.degrees(math.atan2(float(o.y), float(o.x)))
                if previous_raw is None:
                    change = 0.0
                    unwrapped = raw
                    initial_unwrapped = raw
                else:
                    change = raw - previous_raw
                    if change > 180:
                        change -= 360
                    elif change < -180:
                        change += 360
                    unwrapped += change
                    total_absolute_turn += abs(change)
                net = unwrapped - initial_unwrapped
                elapsed = time.time() - start_time
                w.writerow([elapsed, float(p.x), float(p.y), raw, change, net, total_absolute_turn])
                if i % 5 == 0:
                    print(f"{i:03d} heading={raw:7.2f} change={change:+6.2f} net={net:+7.2f} total-turn={total_absolute_turn:7.2f}")
                previous_raw = raw
                await asyncio.sleep(0.2)
        print(f"Finished. Saved {filename}")


if __name__ == "__main__":
    asyncio.run(main())
