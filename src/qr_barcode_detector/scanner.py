from collections.abc import Callable

import cv2
import numpy as np
from pyzbar.pyzbar import decode

Color = tuple[int, int, int]
LabelProvider = Callable[[str], tuple[str, Color]]


def default_label_provider(data: str) -> tuple[str, Color]:
    return data, (255, 0, 255)


def run_realtime_scanner(
    label_provider: LabelProvider = default_label_provider,
    camera_index: int = 0,
    width: int = 640,
    height: int = 480,
    window_name: str = "Result",
) -> None:
    """Run camera stream and annotate all detected QR/barcodes."""
    cap = cv2.VideoCapture(camera_index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    if not cap.isOpened():
        raise RuntimeError("Could not open camera. Check camera index or permissions.")

    try:
        while True:
            success, img = cap.read()
            if not success:
                continue

            for barcode in decode(img):
                data = barcode.data.decode("utf-8")
                label_text, color = label_provider(data)
                print(data)

                points = np.array([barcode.polygon], dtype=np.int32).reshape((-1, 1, 2))
                cv2.polylines(img, [points], True, color, 5)

                x, y, _, _ = barcode.rect
                cv2.putText(
                    img,
                    label_text,
                    (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    color,
                    2,
                )

            cv2.imshow(window_name, img)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
