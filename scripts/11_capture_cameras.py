import os
import numpy as np
import navel

OUTPUT_DIR = "data/camera_tests"
os.makedirs(OUTPUT_DIR, exist_ok=True)

cameras = [
    ("head", navel.HeadCamera),
    ("chest", navel.ChestCamera),
]

for name, Camera in cameras:
    camera = Camera()

    try:
        print(f"\nOpening {name} camera...")
        camera.open()

        frame = camera.get_frame(timeout_ms=2000)
        image = np.asarray(frame.data)

        print("Shape:", image.shape)
        print("Data type:", image.dtype)
        print("Resolution:", frame.width, "x", frame.height)

        # Save original pixel data
        np.save(
            os.path.join(OUTPUT_DIR, f"{name}_camera.npy"),
            image
        )

        # Save a standard PPM image
        image = np.ascontiguousarray(image, dtype=np.uint8)

        with open(
            os.path.join(OUTPUT_DIR, f"{name}_camera.ppm"), "wb"
        ) as file:
            file.write(f"P6\n{frame.width} {frame.height}\n255\n".encode())
            file.write(image.tobytes())

        print(f"Saved {name} camera images successfully.")

    except Exception as error:
        print(f"{name} camera error:", repr(error))

    finally:
        camera.close()
        print(f"{name} camera closed.")

print("\nCamera capture completed.")
