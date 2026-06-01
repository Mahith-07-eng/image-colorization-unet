
import cv2
import numpy as np

def save_output(
    predicted_image,
    output_path
):

    saved_image = np.clip(
        predicted_image * 255,
        0,
        255
    ).astype(np.uint8)

    success = cv2.imwrite(
        output_path,
        saved_image
    )

    if success:
        print(
            f"Saved: {output_path}"
        )
    else:
        print(
            "Failed to save image."
        )