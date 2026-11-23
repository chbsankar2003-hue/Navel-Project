#!/usr/bin/env python3
\"\"\"Read Navel locomotion/range data. This script does NOT move the robot.\"\"\"

import asyncio
import navel


async def main():
    # Open the robot SDK connection.
    async with navel.Robot() as robot:
        print("Connected to Navel. Reading sensor data only; no movement commands.")

        # Read several packets so we can see whether values change.
        for sample_number in range(1, 11):
            data = await robot.next_locomotion(timeout=2.0)

            print(f"\\n--- sample {sample_number} ---")

            # Range data is a dictionary keyed by Navel Sensor enum.
            print("Raw distances dictionary:", data.distances)

            # Print each sensor group separately, if present.
            for sensor, values in data.distances.items():
                print(f"{sensor}: {values}")

            # Odometry may be absent; check before accessing it.
            if data.odometry is None:
                print("Odometry: not present in this packet")
            else:
                print("Odometry object:", data.odometry)
                print("Position:", data.odometry.position)
                print("Orientation:", data.odometry.orientation)
                print("Velocity:", data.odometry.velocity)

            # Wait a little before reading the next packet.
            await asyncio.sleep(0.5)

        print("\\nSensor inspection complete. No movement was commanded.")


if __name__ == "__main__":
    asyncio.run(main())
