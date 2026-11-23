"""Read-only inspection of Navel sensor and odometry packets."""

import asyncio
import navel


def show_distance_groups(distances):
    print("Raw distances:", distances)

    if hasattr(distances, "items"):
        for key, values in distances.items():
            label = getattr(key, "value", str(key))
            print(f"  {label}: {values}")


async def main():
    async with navel.Robot() as robot:

        print("Read-only sensor inspection. No movement commands.")

        for sample in range(10):
            data = await robot.next_locomotion()

            print(f"\n--- sample {sample + 1} ---")

            show_distance_groups(data.distances)

            odom = data.odometry

            p = odom.position
            o = odom.orientation
            v = odom.velocity

            print(
                f"Position: x={p.x:.4f}, "
                f"y={p.y:.4f}, z={p.z:.4f}"
            )

            print(
                f"Orientation: x={o.x:.5f}, "
                f"y={o.y:.5f}, z={o.z:.5f}, w={o.w:.5f}"
            )

            print("Velocity object type:", type(v).__name__)
            print("Velocity object representation:", repr(v))

            await asyncio.sleep(0.2)


if __name__ == "__main__":
    asyncio.run(main())
