import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from qr_barcode_detector.authorization import load_authorized_codes
from qr_barcode_detector.scanner import run_realtime_scanner

AUTHORIZED_CODES = load_authorized_codes(PROJECT_ROOT / "data" / "authorized_codes.txt")


def _label_provider(data: str) -> tuple[str, tuple[int, int, int]]:
    if data in AUTHORIZED_CODES:
        return "Authorized", (0, 255, 0)
    return "Un-Authorized", (0, 0, 255)


if __name__ == "__main__":
    run_realtime_scanner(label_provider=_label_provider)
