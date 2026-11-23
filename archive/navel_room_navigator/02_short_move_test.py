#!/usr/bin/env python3
\"\"\"Supervised short movement test. This does NOT implement obstacle avoidance.\"\"\"

import asyncio
import navel


async def main():
    print("WARNING: This program will move the robot.")
    print("Only run after supervisor approval, with clear space and emergency stop known.")

    async with navel.Robot() as robot:
        print("Connected.")
        print("Command: move forward 0.20 m at 0.10 m/s")
        await robot.move_base(0.20, speed=0.10)
        print("Movement action finished.")


if __name__ == "__main__":
    asyncio.run(main())
