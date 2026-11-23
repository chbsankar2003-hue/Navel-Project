"""Read-only provisional LiDAR classifier. Does not command robot movement."""
import asyncio
from collections import deque
from statistics import median
import navel

CLOSE_M = 0.15       # provisional only; not calibrated
CAUTION_M = 0.25     # provisional only; not calibrated
WINDOW = 5


def lidar_values(distances):
    if hasattr(distances, "items"):
        for key, values in distances.items():
            if "lidar" in str(getattr(key, "value", key)).lower():
                return list(values) if values is not None else []
    return []


def classify(raw, history):
    if raw is None or raw <= 0:
        return "UNAVAILABLE", None
    history.append(raw)
    filtered = median(history)
    if filtered < CLOSE_M:
        return "CLOSE", filtered
    if filtered < CAUTION_M:
        return "CAUTION", filtered
    return "CLEAR_BY_THRESHOLD_ONLY", filtered


async def main():
    async with navel.Robot() as robot:
        histories = [deque(maxlen=WINDOW), deque(maxlen=WINDOW)]
        print("Read-only provisional classifier. Thresholds are not calibrated.")
        print("Zero/invalid readings are UNAVAILABLE, never CLEAR.")
        for i in range(100):
            data = await robot.next_locomotion()
            vals = lidar_values(data.distances)
            outputs = []
            for j in range(2):
                try:
                    raw = float(vals[j])
                except (IndexError, TypeError, ValueError):
                    raw = None
                status, filt = classify(raw, histories[j])
                outputs.append(f"LiDAR[{j}] raw={raw} filtered={filt} status={status}")
            print(f"{i:03d} | " + " | ".join(outputs))
            await asyncio.sleep(0.2)


if __name__ == "__main__":
    asyncio.run(main())
