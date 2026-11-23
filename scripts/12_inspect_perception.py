import asyncio
import navel


async def main():

    async with navel.Robot() as robot:

        print("Connected to Navel perception interface.")
        print("Read-only inspection. No movement commands.")

        for i in range(5):

            print(f"\n========== FRAME {i + 1} ==========")

            try:
                data = await robot.next_frame(timeout=3)

                print("Timestamp:", data.time)

                print("\nDetected persons:", len(data.persons))

                for person in data.persons:
                    print("Person:", repr(person))

                print("\nSound-source timestamp:", data.sst_time_latest)
                print("Sound-source tracks:", repr(data.sst_tracks_latest))

            except Exception as error:
                print("Perception error:", repr(error))


if __name__ == "__main__":
    asyncio.run(main())
